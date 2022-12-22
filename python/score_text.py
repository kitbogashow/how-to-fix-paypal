"""
Score text app.
"""
import json

"""Used for judgement on if an invoice is sus."""
SUSNESS_THRESHOLD = 2.5

def write_json(output: str) -> None:
    with open('python/output/results.json', 'w') as f:
        f.write(output)


def load_sus_words(filepath: str) -> dict[str, float]:
    """Load in sus words with ranking of susness."""
    with open(filepath, 'r') as f:
        items = dict(line.split('=', 1) for line in f.readlines())
        return {i: float(items[i].strip()) for i in items}


def load_invoices(filepath: str) -> list[str]:
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.readlines()


def scan_invoice(invoice: str, sus_words: dict[str, float]) -> float:
    """Scan an invoice and produce a ranking of susness."""
    return sum(score for word, score in sus_words.items() if word in invoice.lower())


def main() -> None:
    """
    Hey Kit!

    Not too much was really added here, mostly just structure. However, my idea
    with this is that there is a threshold for susness. When an invoice is ranked,
    it's measured up to a threshold, and if it passes it, it's flagged. You can check
    out the output of this run in output/results.json.
    """
    sus_words = load_sus_words('python/sus_words.txt')
    invoices = load_invoices('python/input/invoices.txt')
    scores = {f'{invoice[:50]}...': scan_invoice(invoice, sus_words) for invoice in invoices}
    scores_flagged = {score: { 'score': scores[score], 'flagged': scores[score] >= SUSNESS_THRESHOLD } for score in scores}
    write_json(json.dumps(scores_flagged, indent=4))


if __name__ == '__main__':
    main()
