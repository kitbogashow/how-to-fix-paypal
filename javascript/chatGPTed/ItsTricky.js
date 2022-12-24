const fs = require("fs");
//written by chatGPT
//prompt: Write some JavaScript code to identify if the intent of given text is to trick a user into giving money to a bad actor. Some examples of this occurring are:
//- Thank You for Choosing PayPal, Your Payment of $619.99 will be charged through PAYPAL for BITCOIN CRYPTO. If you did not make this transaction, please contact us at this number +1(445) 555-0005 to cancel and claim a refund. If this is not the case, you will be charged $619.99 today. This transaction will reflect on PayPal activity after 24 hours. Our Service Hours: (6:00 a. m. to 06:00 p. m. Pacific Time).
//- We have found some suspicious activites with your account. If you did not make this purchase, please call us at toll free number +1 (862) 555-0005 to cancel and claim a refund. If this is not the case, you will be charged $599.99 today. Within the automated deduction of the amount, this transaction will reflect on PayPal activity within 24hours to 48 hours.Our Service Hour: (06:00 a. m. to 06:00 p. m. Pacific Time, Monday through Sunday)
//- Dear Customer, You sent a payment of $799.00 USD to Coinbase Corporation. If you did not make this payment or to cancel this transaction , please call our Help Desk number: +1(888)555-0005 Cancellation after 24 hours from this email won't be vaild for a refund. Have a great day! PayPal® Help Desk +1(888)555-0005
//- Payment to TREND MICRO® LLC was forwarded to you from PayPal for $449. 77 USD. If you are aware that this payment was not authorized or desire to abolish this charge, Please call the Customer Service Number at +1-888-555-0005
//- We found suspicious activity on your account. If you did not make this transaction, please call us at our toll free number +18 88 555-0005 / +1 808 555-0005 to cancel and claim a refund. If this is not the case, you will be charged AUD 599. 00 today by our automated payment system. This transaction will reflect on PayPal activity after 24 hours.
//- Dear Customer You sent a payment of $479. 00 USD to Geek squad. If you did not make this payment or to cancel this transaction . please call our Help Desk number  +1 (855)555-0005 Cancellation after 48 houors from this email won't be valid for a refund. Have a great day! PayPal Help Desk +1 (855) 555-0005
//- You have successfully made a transaction for your Bitcoin (BTC) Using PayPal, you Charged the amount mentioned in the Invoice. This transaction may take 12 hours to appear in your Bank Statement. Do give us a Call for any dispute regarding the Payment and issue a Refund at +1 (877) 555-0005
//- Transactions from your PayPal account have been discovered by us. If you did not initiate this transaction, please contact us +1 (888) 555-0005 to cancel it; otherwise, your $899. 99 USD will be charged today. Within the automated deduction of the amount, this transaction will reflect on PayPal activity after 24 hours. Our Service Hours: (06:00 a. m. to 06:00 p. m. Pacific Time, Monday through Sunday.
//- We've detected that your PayPal account has been accessed fradulently. If you did not make this transaaction, please call us at toll free number +1 (877) 555-0005 to cancel and claim a refund. If this is not the case, you will be charged $400. 00 USD today. Within the automated deduction of the amount, this transaction will reflect on PayPal activity after 24 hours.
//- According to the information, your PayPal account may have been illegally access. $600.00 has been deducted from your account to cover the cost of iTunes Gift Cards. This transaction will appear on the Payment activity page in the amount that was automatically deducted after 24 hours. If you think you did not make this transaction, call us right away at +1(866) 555-0005, or visit the PayPal Support Center for assistance. Our Business Hours: (06:00 a. m. to 09:00 p. m. , MONDAY through SUNDAY)
//- Dear Customer, Your Payment of $499. 00 of BTC from Coin Base has been approved successfully, This transaction will appear in the automatically deducted amount on PayPal activity and Bank statement after 24 hours. If you suspect you did not make this transaction, Immediately contact us at the toll-free number +1 (866) 555-0005 or visit the PayPal support center area for assistance. +1 (866) 555-0005
//- Your Payment of $399. 99 to TREND MICRO®️ LLC appears to have been unauthorized. If you did not make this transaction contact us @ (888)-[555-0005]
function isTrickText(text) {
    // Check if the text mentions a payment or charge
    if (
        text.toLowerCase().includes("payment") ||
        text.toLowerCase().includes("charge")
    ) {
        // Check if the text mentions a refund or cancellation
        if (
            text.toLowerCase().includes("refund") ||
            text.toLowerCase().includes("cancel")
        ) {
            // Check if the text includes a phone number for contacting customer service
            if (text.match(/\+[0-9]{1,4}\s?[0-9]{3}\s?[0-9]{3}\s?[0-9]{3}/)) {
                return true;
            }
        }
    }
    return false;
}

// prompt: The factors used in identifying could occur in a legitimate given text. Can you include more factors in identifying the messages to prevent false identification.
function isTrickText2(text) {
    // Check if the text mentions a payment or charge
    if (
        text.toLowerCase().includes("payment") ||
        text.toLowerCase().includes("charge")
    ) {
        // Check if the text mentions a refund or cancellation
        if (
            text.toLowerCase().includes("refund") ||
            text.toLowerCase().includes("cancel")
        ) {
            // Check if the text includes a phone number for contacting customer service
            if (text.match(/\+[0-9]{1,4}\s?[0-9]{3}\s?[0-9]{3}\s?[0-9]{3}/)) {
                // Check if the text mentions a suspicious activity or unauthorized transaction
                if (
                    text.toLowerCase().includes("suspicious") ||
                    text.toLowerCase().includes("unauthorized")
                ) {
                    // Check if the text mentions a deadline for cancelling the transaction
                    if (
                        text.toLowerCase().includes("deadline") ||
                        text.toLowerCase().includes("cancellation")
                    ) {
                        return true;
                    }
                }
            }
        }
    }
    return false;
}

//prompt: Could you also add factors to consider messages that try posing as a support team
function isTrickText3(text) {
    // Check if the text mentions a payment or charge
    if (
        text.toLowerCase().includes("payment") ||
        text.toLowerCase().includes("charge")
    ) {
        // Check if the text mentions a refund or cancellation
        if (
            text.toLowerCase().includes("refund") ||
            text.toLowerCase().includes("cancel")
        ) {
            // Check if the text includes a phone number for contacting customer service
            if (text.match(/\+[0-9]{1,4}\s?[0-9]{3}\s?[0-9]{3}\s?[0-9]{3}/)) {
                // Check if the text mentions a suspicious activity or unauthorized transaction
                if (
                    text.toLowerCase().includes("suspicious") ||
                    text.toLowerCase().includes("unauthorized")
                ) {
                    // Check if the text mentions a deadline for cancelling the transaction
                    if (
                        text.toLowerCase().includes("deadline") ||
                        text.toLowerCase().includes("cancellation")
                    ) {
                        // Check if the text includes a support team or help desk
                        if (
                            text.toLowerCase().includes("support team") ||
                            text.toLowerCase().includes("help desk")
                        ) {
                            return true;
                        }
                    }
                }
            }
        }
    }
    return false;
}

//prompt: can you weight the factors so that a threshold must be passed to be identified as trick text
function isTrickText4(text) {
    // Set the threshold for determining if a text is a trick text
    const THRESHOLD = 3;

    // Set the count to 0
    let count = 0;

    // Check if the text mentions a payment or charge
    if (
        text.toLowerCase().includes("payment") ||
        text.toLowerCase().includes("charge")
    ) {
        count++;
    }

    // Check if the text mentions a refund or cancellation
    if (
        text.toLowerCase().includes("refund") ||
        text.toLowerCase().includes("cancel")
    ) {
        count++;
    }

    // Check if the text includes a phone number for contacting customer service
    if (text.match(/\+[0-9]{1,4}\s?[0-9]{3}\s?[0-9]{3}\s?[0-9]{3}/)) {
        count++;
    }

    // Check if the text mentions a suspicious activity or unauthorized transaction
    if (
        text.toLowerCase().includes("suspicious") ||
        text.toLowerCase().includes("unauthorized")
    ) {
        count++;
    }

    // Check if the text mentions a deadline for cancelling the transaction
    if (
        text.toLowerCase().includes("deadline") ||
        text.toLowerCase().includes("cancellation")
    ) {
        count++;
    }

    // Check if the text includes a support team or help desk
    if (
        text.toLowerCase().includes("support team") ||
        text.toLowerCase().includes("help desk")
    ) {
        count++;
    }

    // If the count is greater than or equal to the threshold, return true
    if (count >= THRESHOLD) {
        return true;
    }

    // Otherwise, return false
    return false;
}

//read in invoice text
let texts = fs.readFileSync("../../invoices.txt", { encoding: "utf8" });
texts = texts.split("\n");
//for each text, check if it is a trick text and print the the function that identified it as a trick text
for (let text of texts) {
    if (!isTrickText(text)) {
        console.log("T1");
    }
    if (!isTrickText2(text)) {
        console.log("T2");
    }
    if (!isTrickText3(text)) {
        console.log("T3");
    }
    if (!isTrickText4(text)) {
        console.log("T4");
    }

    console.log("\n");
    console.log(text);
}
