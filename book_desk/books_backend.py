import sqlite3

#===== Create table =================

def connect():
    conn=sqlite3.connect("bookkeeper.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title text, author text, year text, isbn integer)")
    conn.commit()
    conn.close()


def insert(title,author,year,isbn):
    conn=sqlite3.connect("bookkeeper.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO books VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()

def viewAll():
    conn=sqlite3.connect("bookkeeper.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM books")
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def search(title="",author="",year="",isbn=""):
    conn=sqlite3.connect("bookkeeper.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def update(id,title,author,year,isbn):
    conn=sqlite3.connect("bookkeeper.db")
    cur=conn.cursor()
    cur.execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()
""" 
def update(id,title="",author="",year="",isbn=""):
    conn=sqlite3.connect("bookkeeper.db")
    cur=conn.cursor()
    cur.execute("UPDATE books SET title=? OR author=? OR year=? OR isbn=? WHERE id=?",(id,title,author,year,isbn))
    conn.commit()
    conn.close()
 """
def delete(id):
    conn=sqlite3.connect("bookkeeper.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM books WHERE id=?",(id,))
    conn.commit()
    conn.close()


# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# #logging.disable(logging.CRITICAL)

# logging.debug('Start of program')

# def factorial(n):
#     logging.debug('Start of factorial(%s)' % (n))
#     total = 1
#     for i in range( 1, n + 1):
#         total *= i
#         logging.debug('i is %s, total is %s' % (i, total))

#     logging.debug('Return value is %s' % (total))
#     return total

# print(factorial(5))

# logging.debug('End of program')




#connect()
#insert('Airplanes','Henry Lincoln',1968,913123345)
#update(2,"The moon", "Tim Jones",1988,913123146)
#print(viewAll())
#print(search(author="Tim Jones"))