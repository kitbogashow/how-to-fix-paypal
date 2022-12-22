<?php

/**
 * This is based off of the same method that email spam filters used to use - a
 * heuristics-based approach that calculates the "spammyness" of a message based
 * on factors such as:
 *
 * - The number of links in the message
 * - The number of phone numbers in the message
 * - The number of words/characters in the message
 * - The number of words in the message that are not in the dictionary
 * - Suspicious words in the message (BTC, PayPal, etc.)
 *
 * The spam factor ranges between 0.0 and 1.0, where 0.0 is not spam and 1.0 is
 * spam.
 *
 * This solution is intended to be modular (can add new filters as scammers
 * change their tactics).
 *
 * This solution needs tweaking since it lets some messages through. This is
 * otherwise just a proof of concept.
 *
 * ---
 *
 * Running this on the test data (Linux):
 *
 * $ cat ../invoices.txt | php modular_filter.php
 *
 * Output:
 *
 * ```
 * ...
 *   LinkFilter: 0.000000
 *   PhoneFilter: 0.350000
 *   CryptoCurrencyFilter: 0.000000
 *   LengthFilter: 1.000000
 *   SpecialCharacterFilter: 1.000000
 * Message 10: 0.79, is spam? yes
 * ...
 * ```
 *
 * I used PHP 8.2, probably doesn't work on below PHP 7.
 */


/**
 * Main class for the spam analyzer. Runs registered filters on a message and
 * returns a score.
 *
 * @package
 */
class SpamAnalyzer {
  /** @var IFilter[] */
  private $filters = [];

  /**
   * Register a filter to the analyzer.
   *
   * @param IFilter $filter Some object that implements the Filter interface.
   * @return SpamAnalyzer Self for fluent interface.
   */
  public function addFilter(IFilter $filter): SpamAnalyzer {
    $this->filters[] = $filter;

    // Return self for fluent interface.
    return $this;
  }

  /**
   * Analyze a message and return a score. The score should be between 0 and 1,
   * where 0 is not spam and 1 is spam.
   *
   * @param string $message Input message to analyze.
   * @return float
   */
  public function analyze(string $message): float {
    // Calculate L2 norm of the vector of scores. This is the same as the
    // calculate distance function.
    $score = 0;
    foreach ($this->filters as $filter) {
      // Get score and clamp between 0 and 1.
      $individual_score = min(
        1,
        max(0, $filter->filter($message))
      );
      $score += $individual_score * $individual_score;

      // DEBUG: print out the individual scores per each filter.
      echo sprintf("  %s: %f", get_class($filter), $individual_score) . PHP_EOL;
    }

    // And return softmax of the score. This clamps the score to be nicely
    // between 0.0 and 1.0 but never 0.0 or 1.0.
    return 1.0 / (1.0 + exp(-$score)) * 2 - 1;
  }
}

/**
 * Interface for a filter. A filter is an object that analyzes a message and
 * returns a score between 0 and 1, where 0 is not spam and 1 is spam.
 */
interface IFilter {
  /**
   * Analyze a single message and return a score. The score should be between 0
   * and 1, where 0 is not spam and 1 is spam.
   *
   * @param string $message Input message to analyze.
   * @return float Spam score between 0 and 1.
   */
  public function filter(string $message): float;
}

/**
 * Look for links in a message.
 *
 * Pretty sure that PayPal doesn't allow links in messages, but I made this
 * anyways as an example and easy test.
 *
 * @package
 */
class LinkFilter implements IFilter {
  public function filter(string $message): float {
    $message = strtolower($message);
    $links = preg_match_all('/https?:\/\/[^\s]+/', $message, $matches);
    return (float) max(0, $links);
  }
}

/**
 * Look for phone numbers in a message.
 *
 * @package
 */
class PhoneFilter implements IFilter {
  private const WEIGHT_CONTAINS_PHONE = 0.25;
  private const WEIGHT_PER_PHONE = 0.1;

  public function filter(string $message): float {
    // First only keep alphanumeric characters - we don't want people to be able
    // to easily obfuscate telephone numbers.
    $message = strtolower($message);
    $message = preg_replace('/[^a-z0-9]/i', '', $message);
    $num_phones = preg_match_all('/[0-9]{10}/', $message, $matches);

    if ($num_phones > 0) {
      return (float) self::WEIGHT_CONTAINS_PHONE + $num_phones * self::WEIGHT_PER_PHONE;
    } else {
      return 0.0;
    }
  }
}

/**
 * Look for crypto references.
 *
 * @package
 */
class CryptoCurrencyFilter implements IFilter {
  private const WEIGHT_CONTAINS_CRYPTO = 0.25;
  private const WEIGHT_PER_MENTION = 0.1;

  public function filter(string $message): float {
    $cryptos = [
      'btc', 'bitcoin', 'eth', 'ethereum', 'ltc', 'litecoin', 'coinbase', 'kraken',
      'binance', 'bittrex', 'poloniex', 'bitfinex', 'bitstamp', 'coinbasepro',
    ];
    $message = strtolower($message);
    $message = preg_replace('/[^a-z0-9\s]/i', '', $message);
    $num_cryptos = 0;
    foreach ($cryptos as $crypto) {
      $num_cryptos += preg_match_all('/' . $crypto . '/', $message, $matches);
    }

    if ($num_cryptos > 0) {
      return (float) self::WEIGHT_CONTAINS_CRYPTO + $num_cryptos * self::WEIGHT_PER_MENTION;
    } else {
      return 0.0;
    }
  }
}

/**
 * Look at length of the message and assume legitimate requests are generally short.
 *
 * @package
 */
class LengthFilter implements IFilter {
  private const WEIGHT_PER_CHAR = 0.001;
  private const WEIGHT_PER_WORD = 0.01;

  public function filter(string $message): float {
    $num_chars = strlen($message);
    $num_words = str_word_count($message);
    return (float) $num_chars * self::WEIGHT_PER_CHAR + $num_words * self::WEIGHT_PER_WORD;
  }
}

/**
 * Look for special characters in the message.
 *
 * @package
 */
class SpecialCharacterFilter implements IFilter {
  private const WEIGHT_PER_SPECIAL_CHAR = 0.05;

  public function filter(string $message): float {
    $num_special_chars = preg_match_all('/[^\w\d\s]/i', $message, $matches);
    return (float) $num_special_chars * self::WEIGHT_PER_SPECIAL_CHAR;
  }
}


// Main code. Simply check that the file was ran directly rather than imported
// from elsewhere.
if (basename(__FILE__) === basename($_SERVER["SCRIPT_FILENAME"])) {
  // Take in newline-separated messages from stdin.
  /** @var string[] */
  $messages = explode("\n", file_get_contents('php://stdin'));

  // If the score is higher than this threshold, then we consider it spam.
  $threshold = 0.75;

  // Register the previously defined filters.
  $analyzer = new SpamAnalyzer();
  $analyzer->addFilter(new LinkFilter())
    ->addFilter(new PhoneFilter())
    ->addFilter(new CryptoCurrencyFilter())
    ->addFilter(new LengthFilter())
    ->addFilter(new SpecialCharacterFilter());

  // Run the analyzer on each message and print the results.
  foreach ($messages as $index => $message) {
    $score = $analyzer->analyze($message);
    echo sprintf(
      "Message %d: %.02f, is spam? %s",
      $index + 1,
      $score,
      $score > $threshold ? 'yes' : 'no'
    ) . PHP_EOL;
  }
}

/*
 * Some notes:
 *
 * - There needs to be legitimate test request messages to check for false
 *   positives. This is probably what one of the large factors that makes PayPal
 *   reluctant to implement a simple filter-based or really any approach to
 *   combatting fraudulent messages.
 * - Machine learning approaches are cool but often come with restrictive
 *   licenses. Also, any ML classifier trained on invoices will require many,
 *   many examples with real data so it doesn't so weird things like "phone
 *   number is 555? That's spam!".
 * - PayPal probably doesn't want to solve the problem for several reasons
 *   (please don't blame the developers working on the project since they aren't
 *   the ones entirely making the decisions):
 *   - A big red "untrusted invoice" banner on the top of the page reduces
 *     confidence in the whole platform (probably warranted). PayPal execs
 *     probably wouldn't sign off on a feature like this.
 *   - Software at an enterprise level is hard to change - they have
 *     servers/data scattered across the globe, so it's not as simple as just
 *     changing the code and pushing it to GitHub. Although, they have known
 *     about this problem since 2020...
 *   - The cost of a false positive is probably much higher than the cost of
 *     false negatives for them (again, not morally right, but PayPal wants
 *     money). So, they'd rather not implement a solution that has a high false
 *     positive rate, or really any sweeping solution at all.
 */
