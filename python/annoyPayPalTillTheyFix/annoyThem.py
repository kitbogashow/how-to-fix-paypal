#sends an invoice to every 1 hour to annoy paypal till they fix their api
#DO NOT ACTUALLY USE THIS IT IS A JOKE AND EDUCATIONAL PURPOSES ONLY
#reguires paypalpythonsdk to be installed (pip install paypalrestsdk)
#requires paypal developer account and app to be created

import paypalrestsdk as paypalrestsdk
import time as time

#paypal developer account info
paypalrestsdk.configure({
    "mode": "sandbox", # sandbox or live
    "client_id": "YOUR CLIENT ID",
    "client_secret": "YOUR CLIENT SECRET" })

#invoice info
invoice = paypalrestsdk.Invoice({
    "merchant_info": {
        "email": "YOUR EMAIL",
        "first_name": "YOUR FIRST NAME",
        "last_name": "YOUR LAST NAME",
        "business_name": "YOUR BUSINESS NAME",
        "phone": {
            "country_code": "001",
            "national_number": "5032141716"
        }
    },
    "billing_info": [{
        "email": "YOUR EMAIL"
    }],
    "items": [{
        "name": "YOUR ITEM NAME",
        "quantity": 1,
        "unit_price": {
            "currency": "USD",
            "value": 0.01 #amount
        }
    }],
    "note":
    "YOUR NOTE",
    "payment_term": {
        "term_type": "NET_45"
    }
})

#send invoice every 1 hour
while True:
    time.sleep(3600)
    if invoice.create():
        print("Invoice[%s] created successfully" % (invoice.id))
    else:
        print(invoice.error)
    if invoice.send():
        print("Invoice[%s] sent successfully" % (invoice.id))
    else:
        print(invoice.error)