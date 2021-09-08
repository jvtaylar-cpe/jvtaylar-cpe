import sqlite3 as lit

def main():
    try:
        db = lit.connect('dbase.db')
        cur= db.cursor()

        tablequery = "CREATE TABLE users(id INTEGER, name TEXT, email TEXT) "

        cur.execute(tablequery)
        print("Table created successfully")
    except:
        print("Unable to create table")

if __name__ == "__main__":
    main()
    