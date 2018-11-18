
import sqlite3


def delete(item):
    # connection string
    conn = sqlite3.connect("lite1.db")
    # create a cursor obj
    cur = conn.cursor()
    # DELETE ROW from Table TABLE1
    cur.execute("DELETE FROM TABLE1 WHERE item=?",(item,))
    # commit changes
    conn.commit()
    # close connection
    conn.close()

def update(quantity,price,item):
    # connection string
    conn = sqlite3.connect("lite1.db")
    # create a cursor obj
    cur = conn.cursor()
    # DELETE ROW from Table TABLE1
    cur.execute("UPDATE TABLE1 SET quantity=?,price=? where item=?",(quantity,price,item))
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

#delete("wine glass")
update(10,7,"wine glass")
print(view_table())