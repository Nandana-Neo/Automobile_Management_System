# Automobile_Management_System
Check the project report pdf for much detailed view

## CONTENTS OF THE PROGRAM

### Tables:

- Bikes			: To store the details of Bikes available
- Scooter		: To store the details of Scooters available
- Cars			: To store the details of Cars available
- Bank			: To store the details of Bank along with rate provided (for Emi)
- Ally_Companies	: To store the details of Ally Companies 
- Customers		: To store the details of Customers
- Employee		: To store the details of Employees

### Functions:

- employee()		: To input employee details
- agency_pov()	: Deals with functions related to agency point of view. 
      Performs the functions:
      1)	To add Employee details
      2)	To view Employee details
      3)	To view Customer details
      4)	To view number of vehicles sold so far
      5)	To view Ally Companies
      6)	To view Amount Collected so far with the Biggest Sale Of the Day
  
- Comparison()	: To compare the details of inputted 2 vehicles
- Customers()		: To insert data into Customers table
- updateagent()	: To update the number of vehicles sold for entered agent in Employee table
- EMIfunc()		: To calculate the Emi 
- Customerpov()	: Deals with functions related to customer point of view. The customer can compare vehicles and place the order for buying a vehicle. Finally, the BILL is printed.
			  
* Note- The entire program is run together.

## How to run
- PreReq: MySQL, Python and Python-MySQL needs to be installed
- A database called ‘project’ is created in MySQL and the program uses it.
  ```
  CREATE DATABASE project;
  USE project;
  ```
- Run `create_tables.py`
  > Note: This file is to be run only once because this file uploads data into the table. So DO NOT run more than once to avoid data replication
- Run `main.py` and the main function will be called. The user interface can occur through a python shell
