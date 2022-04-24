# Table of contents

- [Table of contents](#table-of-contents)
- [PAYMETS](#paymets)
- [Introduction](#introduction)
  - [Who is to use it](#who-is-to-use-it)
    - [Frameworks used](#frameworks-used)
    - [Requirements](#requirements)
- [Installation](#installation)
  - [Configuring the project](#configuring-the-project)
- [Using the Paymets project](#using-the-paymets-project)
  - [Starting a django server](#starting-a-django-server)

# PAYMETS
# Introduction
Paymets is a django projects which is used to create paymetApi usable app/library.<br>
PaymetApi is a REST API that consumes [fluterwave](https://flutterwave.com/ug/) API.
## Who is to use it
<!-- Paymets is a REST API for mobile money payments in Uganda, it also consumes a nother API of [flutterwave](https://flutterwave.com/ug/). <br> -->
If you are a python developer who is developing a mobile money payment system for Uganda while consuming [flutterwave](https://flutterwave.com/ug/) APIs, this is REST API that you can use to finish your goal.
Are you a python developer and you want to contribute to this project?!, this is for you..
> **_NOTE:_**  This project is for mobile money payments in Uganda now, more features are still being developed.

### Frameworks used
Django and django rest framework are the frameworks used for this project.
### Requirements

* python >= 3.8
* Django
* Django rest framework
* Flutterwave account

# Installation
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

 After we have finished to install our project successfuly, we have to configure our with the right configuration so that our project can work very well.<br>
 This project uses a .env file to store enviromental variables and our secret keys.
 In the root directory of the project navigate to the root directory of folder payments which will contain files like settings, in that root directory, create a .env file, in the .env file create enviromental variable and name it PAYMET_API_KEY as the example below.
 ``` 
 PAYMET_API_KEY=yourAPIKey 
 ```
 Remember you have to have an account with flutterwave, if you don't have an account with flutterwave, you can create one from [flutterwave](https://flutterwave.com/ug/) and if you have one, get your secret key from the flutterwave dashboard and place it where yourAPIKey is.

 # Using the Paymets project
 After you have finished all the above processes we have mentioned, that means the project is read to get used.<br>
## Starting a django server
  For our project to start we have to start a server that will run our project and we can do so by going to the root directory of our project and run the following command in the commalind line interface 
  ```
  python manage.py runserver 
  ```
  The server will run on `` http://127.0.0.1:8000/ `` URL.<br>
  Copy the URL and run it in your browser adding and end point like this `` http://127.0.0.1:8000/api
 ``,
 your screen should show some thing like the image below
 
![image info](../paymets/imgs/paymet%20welcome%20screen.PNG)

the above image shows a welcome message that shows you that you have installed the project successfuly.

    
   


