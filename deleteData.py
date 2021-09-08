import sqlite3 as lit

db = lit.connect('dbase.db')

with db:
    user_id = 2
    cur = db.cursor()
    # cur.execute("DELETE FROM users where id = ? ", (user_id))
    cur.execute('''DELETE FROM users WHERE id = ? ''', (user_id,))

    db.commit()
    
    print("Data Deleted")