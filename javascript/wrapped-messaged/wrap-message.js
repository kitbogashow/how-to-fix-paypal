//run using node
"use strict";
//import the file system module
const fs = require("fs");
//function to read the message from the file
function readMessage(filepath) {
    let message = fs.readFileSync(filepath, { encoding: "utf-8" });
    //convert the message into array of lines
    message = message.split("\n");
    //return the message array
    return message;
}

//generate the intro message
function generateIntroMessage() {
    //create a string for the intro message
    let introMessage = "";
    introMessage = "<h1 style='color: red; font-weight: bold;'>NOTICE</h1>";
    introMessage +=
        "<div style='font-weight: bold;'> This is a invoice. You have not been charged and may not need to pay. Scammers have used the invoice feature to steal money in the past. ";
    introMessage +=
        "DO NOT Call the number on the invoice or send money to the address on the invoice if you did not request the service or goods. If you have been scammed, please report it to the FTC at ftc.gov/complaint.";
    introMessage +=
        "If you suspect this invoice is please contact the FTC at ftc.gov/complaint and notify paypay using this link: *legit link here*</div>";
    return introMessage;
}

//function to generate the border
function generateBorder(message) {
    return `<h3> User Message</h3><div style='border: 1px solid #000; padding: 10px;'>${message}</div>`; //return the message with the border added Note: basic with no sanitization
}
//function to perform the wrapping

function wrap(message) {
    //generate the intro message
    let introMessage = generateIntroMessage();
    //generate the border
    message = generateBorder(message);
    //concatenate the intro message and the user message
    message = introMessage + message;
    //return the wrapped message
    return message;
}

//function to write the wrapped message to the file
function writeMessage(filepath, message) {
    fs.writeFileSync(filepath, message);
}

//function to do the thing
function doTheThing() {
    //read the message from the file
    let messages = readMessage("../../invoices.txt");
    //for each line in the message
    for (let i = 0; i < messages.length; i++) {
        //if the line is empty
        let message = messages[i];
        if (message === "") continue;
        //wrap the message
        message = wrap(message);
        //write the message to the file
        writeMessage(`./messages/wrapped-message-${i}.html`, message);
    }
}

//call the function to do the thing
doTheThing();
