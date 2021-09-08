import sqlite3 as lit

def main():
    try:
        db= lit.connect('dbase.db')
        print("Database created", db)
    except:
        print("Failed to create Database")

if __name__ == "__main__":
    main()
