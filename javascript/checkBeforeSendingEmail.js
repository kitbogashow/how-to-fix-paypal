// Requires Node and nodemailer to be installed.
// Run `npm i nodemailer` to install after node is installed.
// run with `node sendEmail.js`

const nodemailer = require('nodemailer');
let scamDetected = false;
let redText = '\x1b[31m';

/**
    With real PayPal (service.paypal.com)  information you would use something more like this.
    let mailer = nodemailer.createTransport({
        type: 'OAuth2',
        user: process.env.MAIL_USERNAME,
        pass: process.env.MAIL_PASSWORD,
        clientId: process.env.OAUTH_CLIENTID,
        clientSecret: process.env.OAUTH_CLIENT_SECRET,
        refreshToken: process.env.OAUTH_REFRESH_TOKEN
    });
 */

/** With your own email if you want to test sending an email to yourself. 
    let mailer = nodemailer.createTransport({
    service: 'gmail',
    auth: {
        user: 'youremail@gmail.com',
        pass: 'password',
    },
    });
 */

let mailOptions = {
  from: 'youremail@gmail.com',
  to: 'target@gmail.com',
  subject: 'Invoice from Billing Department of PayPal',
  text: `Dear Customer, Your Payment of $499. 00 of BTC from Coin Base has been approved successfully, This transaction will appear in the automatically deducted amount on PayPal activity and Bank statement after 24 hours. If you suspect you did not make this transaction, Immediately contact us at the toll-free number +1 (866) 555-0005 or visit the PayPal support center area for assistance. +1 (866) 555-0005`,
};

if (String(mailOptions.subject).toLowerCase().includes('paypal')) scamDetected = true;
if (String(mailOptions.text).toLowerCase().replace(/ /g, '').includes('paypalsupportcenter')) scamDetected = true;

if (!scamDetected) {
  console.log('Sending email');
  //   mailer.sendMail(mailOptions, (error, info) => {
  //     error ? console.log(error) : console.log('Email sent: ' + info.response);
  //   });
} else {
  console.log('Detected');
  console.log(`${redText}This message may be a scam!!`);
}
