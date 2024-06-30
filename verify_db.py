import sqlite3

def verify_db():
    conn = sqlite3.connect('funds.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM funds')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()

if __name__ == '__main__':
    verify_db()
