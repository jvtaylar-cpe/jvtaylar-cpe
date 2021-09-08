import sqlite3 as lit

connection = lit.connect("dbase.db")
cursor = connection.cursor()
cursor.execute("SELECT * FROM users;")
results = cursor.fetchall()
for r in results:
    print(r)
cursor.close()
connection.close()