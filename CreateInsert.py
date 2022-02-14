import sqlite3

from sqlite3 import Error


def sql_connection():   #Establish a connection
    try:                #Exception handling (try,except,finally)
        conn = sqlite3.connect('Sales.db') #Create or Open existing database
        return conn
    except Error:
        print(Error)


def sql_table(conn):  #Sales.db
    cursorObj = conn.cursor() #points to the database Sales.db
    # Create the table in Sales.db
   #  cursorObj.execute("CREATE TABLE salesman(salesman_id n(5), name char(30), city char(35), commission decimal(7,2));")
   #  # Insert records
   #  cursorObj.executescript("""
   # INSERT INTO salesman VALUES(5001,'James Hoog', 'New York', 0.15);
   # INSERT INTO salesman VALUES(5002,'Nail Knite', 'Paris', 0.25);
   # INSERT INTO salesman VALUES(5003,'Pit Alex', 'London', 0.15);
   # INSERT INTO salesman VALUES(5004,'Mc Lyon', 'Paris', 0.35);
   # INSERT INTO salesman VALUES(5005,'Paul Adam', 'Rome', 0.45);
   # """)
   #  conn.commit() #STORE THE DATA PERMANENTLY
    cursorObj.execute("SELECT name,city FROM salesman WHERE salesman_id > 5001 and salesman_id <5004") # * -> all columns ->WHERE CLAUSE-SELECTED ROWS
    rows = cursorObj.fetchall()  # rows-> all the records in the salesman table
    print("Agent details:")
    for row in rows:
        print(row)


sqllite_conn = sql_connection() #Sales.db
sql_table(sqllite_conn) #Sales.db
if (sqllite_conn):
    sqllite_conn.close()
    print("\nThe SQLite connection is closed.")
