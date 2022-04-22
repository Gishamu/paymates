# Table of contents

- [Table of contents](#table-of-contents)
- [Introduction](#introduction)
  - [Software name](#software-name)
  - [Who is to use it](#who-is-to-use-it)
    - [Frameworks used](#frameworks-used)
    - [Requirements](#requirements)
- [How to install](#how-to-install)
  - [Configuring the project](#configuring-the-project)
- [Using the Paymet API](#using-the-paymet-api)

# Introduction
## Software name
Paymets
## Who is to use it

Paymets is a REST API for mobile money payments in Uganda, it also consumes a nother API of [flutterwave](https://flutterwave.com/ug/). <br>
If you are a python developer who is developing a mobile money payment for Uganda while consuming [flutterwave](https://flutterwave.com/ug/) APIs, this is REST API tool that you can use to finish your goal.

### Frameworks used

Django and django rest framework are the frameworks used for this project.
### Requirements

* python >= 3.8
* Django
* Django rest framework
* Flutterwave account

# How to install
After meeting all the needs, its time to install this project to your PC (Personal computer)
* step1:<br>
   On your PC creat a virtual enviroment in your preferable directory using a command line terminal.In this document we are not going to go into details on how to create a virtual enviroment using a terminal, you can make research on that.
* step2:<br>
   In your prefarable directory clone this project, after the project has finished cloning go to its directory.

* step3:<br>
   Open your terminal and activate your virtual enviroment that you created in the previous step.
   After you have reached in the directory of the project you can run ``` pip install requirements ``` in the command line terminal. <br>
   This command installs all the dependences that are needed by the project to run.<br>
   After all dependences have been installed, the project is good to start if all  the steps have gone well.

## Configuring the project

 After we have finished to install our project succefuly, we have to configure our with the right configuration so that our project can work very well.<br>
 This project uses a .env file to store enviromental variables and our secret keys.
 In the root directory of the project navigate to the root directory of folder payments which will contain files like settings, in that root directory, create a .env file, in the .env file create enviromental variable and name it PAYMET_API_KEY as the example below.
 ``` 
 PAYMET_API_KEY=yourAPIKey 
 ```
 Remember you have to have an account with flutterwave, if you don't have an account with flutterwave, you can create one from [flutterwave](https://flutterwave.com/ug/) and if you have one, get your secret key from the flutterwave dashboard and place it where yourAPIKey is.

 # Using the Paymet API
 


    
   


