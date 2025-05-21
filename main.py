import pandas as pd
import mysql.connector as sqltor

# Connecting to MySQL database
mycon = sqltor.connect(host='localhost', user='root', passwd='heer@1807', database='cafe')
mycursor = mycon.cursor()

if mycon.is_connected():
    print('Successfully connected to MySQL Database')
else:
    print('MySQL connection problem')


def try_again():
    input('Invalid choice. Press Enter to try again...')
    entry()


def payment():
    df8 = pd.read_sql('SELECT * FROM bill;', mycon)
    print(df8)
    df9 = pd.read_sql('SELECT SUM(price) AS Amount FROM bill;', mycon)
    tbp = int(df9.Amount[0])
    name = input('Enter name: ')
    finalbill = (name, tbp)
    sql = 'INSERT INTO finalbill(Name, Amount) VALUES (%s, %s);'
    mycursor.execute(sql, finalbill)
    mycon.commit()
    df10 = pd.read_sql('SELECT * FROM finalbill;', mycon)
    print('Final Bill: ')
    print(df10)
    input('Press Enter to exit...')
    exit_app()


def home_delivery():
    df4 = pd.read_sql('SELECT * FROM menu;', mycon)
    print(df4)
    mc = int(input('Enter choice (0 for COFFEE, 1 for TEA, etc.): '))

    tables = ['coffee', 'tea', 'freshjuice', 'frappe', 'milkshake', 'burger', 'pizza', 'salad', 'dessert']

    if 0 <= mc < len(tables):
        table_name = tables[mc]
        df5 = pd.read_sql(f'SELECT * FROM {table_name};', mycon)
        print(df5)
        fo = input('Enter Code: ')
        df6 = df5.set_index('code')
        q = int(input('Enter Quantity: '))
        fi = str(df6.item[fo])
        fp = int(df6.price[fo])
        sql = 'INSERT INTO bill(Item, Quantity, Price) VALUES (%s, %s, %s);'
        val = (fi, q, fp * q)
        mycursor.execute(sql, val)
        mycon.commit()
        print('Order successful!')
        proceed()
    else:
        try_again()


def proceed():
    print('''\n1. Order Food
2. Proceed to payment
3. Book Table
4. Cancel Order and Exit''')
    op = int(input('Enter Choice: '))
    if op == 1:
        home_delivery()
    elif op == 2:
        payment()
    elif op == 3:
        book_table()
    else:
        exit_app()


def book_table():
    date = input('Enter date for reservation (dd/mm): ')
    df2 = pd.read_sql('SELECT * FROM tabletype;', mycon)
    print(df2)

    tt = int(input('Choose table type (0-4): '))
    types = ['TABLE FOR TWO', 'TABLE FOR FOUR', 'TABLE FOR SIX', 'TABLE FOR EIGHT', 'TABLE FOR TEN']
    charges = [25, 35, 50, 60, 75]

    if 0 <= tt < len(types):
        ttn = types[tt]
        rc = charges[tt]
        noft = int(input('Enter number of tables: '))
        print(f'{noft} tables to be booked for {date}')
        op3 = input('Confirm Booking? (Y/N): ')
        if op3.upper() == 'Y':
            cust = (ttn, noft, rc * noft)
            sql = 'INSERT INTO bill(Item, Quantity, Price) VALUES (%s, %s, %s);'
            mycursor.execute(sql, cust)
            mycon.commit()
            print('Tables booked.')
            proceed()
        elif op3.upper() == 'N':
            print('''1. Book Again
2. Go to Main Menu''')
            op4 = int(input('What would you like to do? '))
            if op4 == 1:
                book_table()
            else:
                entry()
        else:
            print('Invalid input.')
            proceed()
    else:
        print('Invalid choice.')
        try_again()


def entry():
    print('''
WELCOME TO THE BREW HOUSE!

1. Order for Home Delivery
2. Book Tables
3. Exit''')
    op1 = int(input('What would you like to do? '))
    if op1 == 1:
        home_delivery()
    elif op1 == 2:
        book_table()
    elif op1 == 3:
        exit_app()
    else:
        print('Invalid choice, try again!')
        try_again()


def exit_app():
    print('Thank You for visiting The Brew House!')


# Start the program
entry()
