import sqlite3 as lit

myuser= ((1 ,'Jonathan', 'myemail@gmail.com'),
        ( 2,'John', 'myemail@gmail.com'), 
        ( 3,'Peter', 'myemail@google.com'),)
db = lit.connect('dbase.db')

with db:
    cur= db.cursor()
    cur.executemany("INSERT INTO users VALUES (?,?,?)",myuser)
    print("Data inserted successfully")