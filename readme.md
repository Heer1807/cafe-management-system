# Cafe Management System

This is a command-line based Cafe Management System developed using Python and MySQL. It allows users to place online orders (home delivery), book tables, and generate bills. The system stores data using a MySQL database and interacts with it through Python.

## Features

- Place online orders from a menu (coffee, tea, juice, shakes, etc.)
- Book tables with fixed reservation charges
- View, calculate, and print final bills
- All data is stored in and retrieved from MySQL tables

## Technologies Used

- Python 3
- MySQL
- Pandas
- mysql-connector-python

## Project Structure

cafe-management-system/
├── cafe.sql # SQL script to create and populate the database
├── main.py # Python script with complete application logic
└── README.md # Project documentation


## How to Run

### Step 1: Set Up the MySQL Database

1. Open MySQL command line or MySQL Workbench.
2. Run the following command to execute the SQL file:

```sql
SOURCE E:/PROJECTS/cafe-management-system/cafe.sql;

### Step 2: Install Required Python Packages

Run the following command to install dependencies:

pip install mysql-connector-python pandas

### Step 3: Run the Application

Run the Python script:

python main.py