# Table of contents

- [Table of contents](#table-of-contents)
- [paymates](#paymates)
- [Introduction](#introduction)
  - [Who can use it](#who-can-use-it)
    - [Frameworks used](#frameworks-used)
    - [Requirements](#requirements)
- [Installation](#installation)
  - [Configuring the project](#configuring-the-project)
- [Using the paymates project](#using-the-paymates-project)
  - [Starting a django server](#starting-a-django-server)
- [End points to call](#end-points-to-call)
  - [Charge end point](#charge-end-point)
  - [transaction-history end point](#transaction-history-end-point)
  - [verify end point](#verify-end-point)

# paymates
# Introduction
paymates is a django project which is used to create paymatesApi library.<br>
It was started in 2022 based on mobile money payments in Uganda.
paymatesApi library is a REST API that consumes [fluterwave](https://flutterwave.com/ug/) API.
## Who can use it
<!-- paymates is a REST API for mobile money payments in Uganda, it also consumes a nother API of [flutterwave](https://flutterwave.com/ug/). <br> -->
If you are a python developer who is developing a mobile money payment system while consuming [flutterwave](https://flutterwave.com/ug/) APIs, this is REST API that you can use to reach your goal.
This project is open to contributions.
> **_NOTE:_**  At the moment this project is based on mobile money payments in Uganda.

### Frameworks used

* Django.
* Django restframework
### Requirements

* python >= 3.8
* Django
* Django rest framework
* Flutterwave account

# Installation
After meeting all the requirements, its time to install this project to your PC
* Step1:<br>
   On your PC create a virtual environment in your preferable directory using a command line terminal. In this document we are not going to go into details on how to create a virtual environment using a terminal, you can do research on that.
* Step2:<br>
   In your preferable directory, clone this project. After the project is done, go to its directory root.

* Step3:<br>
   Open your terminal and activate your virtual environment  that you created in step one. Use command ``<name_of_virtual_enviroment>\Scripts\activate.bat ``  for windows. 
    Run ``` pip install requirements ``` in the command line terminal. <br>
   This command installs all the dependences that are needed by the project to run.<br>
   After all dependences have been installed, the project is good to go.

## Configuring the project

 After succeful installation, we have to configure the project with the right configuration so that our project can work very well.<br>
 This project uses a ``.env file`` to store environmental variables and secret keys.
 In the root directory of the cloned project, navigate to the root directory of paymates which will contain files like settings, in the same root directory create a ``.env file``, in the .env file create environmental variable and name it paymates_API_KEY as the example below.
 ``` 
 paymates_API_KEY=yourAPIKey 
 ```
 Remember you have to have an account with flutterwave, if you don't have an account with flutterwave, you can create one from [flutterwave](https://flutterwave.com/ug/) and if you have one, get your secret key from the flutterwave dashboard and place it where yourAPIKey is.

 # Using the paymates project
 After you have finished all the above processes we have mentioned,the project is ready to get used.<br>
## Starting a django server
  For the project to start, go to the root directory of the cloned project and run the following command in the command line interface. 
  ```
  python manage.py runserver 
  ```
  The server will run on `` http://127.0.0.1:8000/ `` URL.<br>
  Copy the URL and run it in your browser, adding an end point like this `` http://127.0.0.1:8000/api
 ``,
 your screen should show some thing like the image below
 
![image info](/imgs/paymet%20welcome%20screen.PNG)

the above image shows a welcome message that lets you know the project was installed successfully.
# End points to call
As any REST API, there are end points to consume and they are listed below
* [charge](#charge-end-point)
* [transaction-history/str:customerName](#transaction-history-end-point)
* [verify](#verify-end-point)
  
## Charge end point
The charge end point is a POST end point that we call when we are initiating payment. Below is an example on how we can call the end point 
```
http://127.0.0.1:8000/api/charge
```
Below is the body that has to be sent with this POST end point.
```
{
    "amount": 7000,
    "currency": "UGX",
    "phoneNumber": "07777777777",
    "email": "testertester@gmail.com",
    "fullName": "Mugisha tester",
    "network": "Airtel",
    "redirect_url": "https://528e-41-210-145-113.ngrok.io/api/verify",
    "description": "this is for testing"
}
```
> **_NOTE:_** redirect_url key value is the URL that recieves details of a transaction after it has been made. verify is the end point of paymate API. This is where you put webhook url if you have one. 


After a POST request is made with the above body, the paymate API will communicate with the flutterwave API, and if there is nothing that has gone wrong, the below response is returned
```
{
    "status": "success",
    "message": "Charge initiated",
    "meta": {
        "authorization": {
            "redirect": "https://ravemodal-dev.herokuapp.com/captcha/verify/47563:a80c5eeb68739909397deb36921864dc",
            "mode": "redirect"
        }
    }
}
``` 
The ``meta.authorization`` object contains the details needed to complete the transaction. The ``mode`` is ``"redirect"``, meaning you should redirect your customer to the provided URL to complete the payment.
To complete the payment, the customer authorizes it with their mobile money provider at the provided redirect URL. For example when you go to the redirect URL you get the below inteface

![image info](/imgs/flutterwave%20OTP.PNG)
In the above interface, you can Enter the OTP sent to you via SMS on mobile so that the transaction can be completed. For the testing case, you can use ``123456`` as your OTP.
When the payment is completed, we'll send you a webhook notification. Here's what the response looks like:
```
{
    "verificationStatus": true,
    "data": {
        "status": "success",
        "message": "Tx Fetched",
        "data": {
            "id": 3322850,
            "txRef": "a7e0374c-c6ec-11ec-9df1-40f02f8abbfe",
            "orderRef": "URF_MMGH_1651148068139_7747135",
            "flwRef": "flwm3s4m0c1651148068308",
            "redirectUrl": "http://127.0.0",
            "device_fingerprint": "N/A",
            "settlement_token": null,
            "cycle": "one-time",
            "amount": 6000,
            "charged_amount": 6000,
            "appfee": 180,
            "merchantfee": 0,
            "merchantbearsfee": 1,
            "chargeResponseCode": "00",
            "raveRef": null,
            "chargeResponseMessage": "Pending Payment Validation",
            "authModelUsed": "MOBILEMONEY",
            "currency": "UGX",
            "IP": "52.209.154.143",
            "narration": "elselearn",
            "status": "successful",
            "modalauditid": "f22aaae8ed2909caf903e23053a9fabb",
            "vbvrespmessage": "N/A",
            "authurl": "NO-URL",
            "vbvrespcode": "N/A",
            "acctvalrespmsg": "Approved",
            "acctvalrespcode": "00",
            "paymentType": "mobilemoneyug",
            "paymentPlan": null,
            "paymentPage": null,
            "paymentId": "N/A",
            "fraud_status": "ok",
            "charge_type": "normal",
            "is_live": 0,
            "retry_attempt": null,
            "getpaidBatchId": null,
            "createdAt": "2022-04-28T12:14:28.000Z",
            "updatedAt": "2022-04-28T12:14:31.000Z",
            "deletedAt": null,
            "customerId": 1605320,
            "AccountId": 101062,
            "customer.id": 1605320,
            "customer.phone": "07777777770",
            "customer.fullName": "Anonymous Customer",
            "customer.customertoken": null,
            "customer.email": "testertester@gmail.com",
            "customer.createdAt": "2022-04-25T13:30:31.000Z",
            "customer.updatedAt": "2022-04-25T13:30:31.000Z",
            "customer.deletedAt": null,
            "customer.AccountId": 101062,
            "meta": [],
            "flwMeta": {}
        }
    }
}
```
From there, we can now verify the transaction by looking at key status value of the data object.

## transaction-history end point
transaction-history is a GET request that you can use to call the paymateAPI like ``http://127.0.0.1:8000/api/transaction-history/[[fullname]]`` where [[fullname]] is a specific fullname of the person you are trying to retrieve.
When you call that end point, the response example below is returned
```
{
    "status": "success",
    "message": "Transactions fetched",
    "meta": {
        "page_info": {
            "total": 23,
            "current_page": 1,
            "total_pages": 3
        }
    },
    "data": [
        
        {
            "id": 3319651,
            "tx_ref": "3a19d167",
            "flw_ref": "flwm3s4m0c1651052923356",
            "device_fingerprint": "N/A",
            "amount": 2000,
            "currency": "UGX",
            "charged_amount": 2000,
            "app_fee": 60,
            "merchant_fee": 0,
            "processor_response": "Approved",
            "auth_model": "MOBILEMONEY",
            "ip": "52.209.154.143",
            "narration": "elselearn",
            "status": "successful",
            "payment_type": "mobilemoneyug",
            "created_at": "2022-04-27T09:48:43.000Z",
            "amount_settled": 1940,
            "customer": {
                "id": 1587590,
                "email": "derrimugisha@gmail.com",
                "phone_number": "704838784",
                "name": "Mugisha Derick",
                "created_at": "2022-04-13T14:50:13.000Z"
            },
            "account_id": 101062,
            "meta": null
        },
        {
            "id": 3311500,
            "tx_ref": "f2ab1f95",
            "flw_ref": "flwm3s4m0c1650815686922",
            "device_fingerprint": "N/A",
            "amount": 2000,
            "currency": "UGX",
            "charged_amount": 2000,
            "app_fee": 60,
            "merchant_fee": 0,
            "processor_response": "Approved",
            "auth_model": "MOBILEMONEY",
            "ip": "52.209.154.143",
            "narration": "elselearn",
            "status": "successful",
            "payment_type": "mobilemoneyug",
            "created_at": "2022-04-24T15:54:46.000Z",
            "amount_settled": 1940,
            "customer": {
                "id": 1587590,
                "email": "derrimugisha@gmail.com",
                "phone_number": "704838784",
                "name": "Mugisha Derick",
                "created_at": "2022-04-13T14:50:13.000Z"
            },
            "account_id": 101062,
            "meta": null
        }
    ]
}
```
 ## verify end point
 verify is a GET request for paymateAPI, which is made to return a response for verification after the completion of the transaction.
 This end point acts as a webhook if you set it in the ``redirect_url`` of the body of the charge end point. For reference: [charge body](#charge-end-point) example.
 It also returns response like this:
 ```
 {
    "verificationStatus": true,
    "data": {
        "status": "success",
        "message": "Tx Fetched",
        "data": {
            "id": 3322850,
            "txRef": "a7e0374c-c6ec-11ec-9df1-40f02f8abbfe",
            "orderRef": "URF_MMGH_1651148068139_7747135",
            "flwRef": "flwm3s4m0c1651148068308",
            "redirectUrl": "http://127.0.0",
            "device_fingerprint": "N/A",
            "settlement_token": null,
            "cycle": "one-time",
            "amount": 6000,
            "charged_amount": 6000,
            "appfee": 180,
            "merchantfee": 0,
            "merchantbearsfee": 1,
            "chargeResponseCode": "00",
            "raveRef": null,
            "chargeResponseMessage": "Pending Payment Validation",
            "authModelUsed": "MOBILEMONEY",
            "currency": "UGX",
            "IP": "52.209.154.143",
            "narration": "elselearn",
            "status": "successful",
            "modalauditid": "f22aaae8ed2909caf903e23053a9fabb",
            "vbvrespmessage": "N/A",
            "authurl": "NO-URL",
            "vbvrespcode": "N/A",
            "acctvalrespmsg": "Approved",
            "acctvalrespcode": "00",
            "paymentType": "mobilemoneyug",
            "paymentPlan": null,
            "paymentPage": null,
            "paymentId": "N/A",
            "fraud_status": "ok",
            "charge_type": "normal",
            "is_live": 0,
            "retry_attempt": null,
            "getpaidBatchId": null,
            "createdAt": "2022-04-28T12:14:28.000Z",
            "updatedAt": "2022-04-28T12:14:31.000Z",
            "deletedAt": null,
            "customerId": 1605320,
            "AccountId": 101062,
            "customer.id": 1605320,
            "customer.phone": "07777777770",
            "customer.fullName": "Anonymous Customer",
            "customer.customertoken": null,
            "customer.email": "testertester@gmail.com",
            "customer.createdAt": "2022-04-25T13:30:31.000Z",
            "customer.updatedAt": "2022-04-25T13:30:31.000Z",
            "customer.deletedAt": null,
            "customer.AccountId": 101062,
            "meta": [],
            "flwMeta": {}
        }
    }
}
```

