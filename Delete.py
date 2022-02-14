import sqlite3
from sqlite3 import Error
def sql_connection():
   try:
     conn = sqlite3.connect('Sales.db')
     return conn
   except Error:
     print(Error)
def sql_table(conn):
   cursorObj = conn.cursor()
   cursorObj.execute("SELECT * FROM salesman")
   rows = cursorObj.fetchall()
   print("Agent details:")
   for row in rows:
       print(row)
   print("\nDelete Salesman of ID 5003:")
   s_id = 5003
   cursorObj.execute("""
   DELETE FROM salesman
   WHERE salesman_id = ?
   """, (s_id,))
   conn.commit()
   cursorObj.execute("SELECT * FROM salesman")
   rows = cursorObj.fetchall()
   print("\nAfter updating Agent details:")
   for row in rows:
       print(row)
sqllite_conn = sql_connection()
sql_table(sqllite_conn)
if (sqllite_conn):
 sqllite_conn.close()
 print("\nThe SQLite connection is closed.")
