
import sqlite3

def create_table():
    #connection string
    conn=sqlite3.connect("lite1.db")
    #create a cursor obj
    cur=conn.cursor()
    #create TABLE TABLE1 - item is text ,quantity is integer,price float VALUEs
    cur.execute("CREATE TABLE IF NOT EXISTS TABLE1 (item TEXT ,quantity INTEGER , price REAL)")
    #commit changes
    conn.commit()
    #close connection
    conn.close()

def insert_table(item,quantity,price):
    # connection string
    conn = sqlite3.connect("lite1.db")
    # create a cursor obj
    cur = conn.cursor()
    # update values to Table TABLE1
    cur.execute("INSERT INTO TABLE1 VALUES(?,?,?)",(item,quantity,price))
    # commit changes
    conn.commit()
    # close connection
    conn.close()

def view_table():
    # connection string
    conn = sqlite3.connect("lite1.db")
    # create a cursor obj
    cur = conn.cursor()
    # query all rows+columns
    cur.execute("select * from TABLE1")
    rows=cur.fetchall()
    # close connection
    conn.close()
    return rows

create_table()
insert_table('wine glass',10,5)
insert_table('plain glass',5,1)
insert_table('coffee cup',5,2)
print(view_table())