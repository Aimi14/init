import sqlite3
import psycopg2

def export_data_to_postgres():
    # Connect to SQLite database
    sqlite_conn = sqlite3.connect('funds.db')
    sqlite_cursor = sqlite_conn.cursor()
    sqlite_cursor.execute('SELECT * FROM funds')
    rows = sqlite_cursor.fetchall()

    # Connect to PostgreSQL database
    postgres_conn = psycopg2.connect(
        dbname='fund_management',
        user='postgres',
        password='Aimi14',
        host='127.0.0.1',
        port='5432'
    )
    postgres_cursor = postgres_conn.cursor()

    for row in rows:
        postgres_cursor.execute('''
            INSERT INTO funds (name, manager_name, description, nav, date_of_creation, performance)
            VALUES (%s, %s, %s, %s, %s, %s)
        ''', row[1:])

    postgres_conn.commit()
    postgres_cursor.close()
    postgres_conn.close()
    sqlite_conn.close()

if __name__ == '__main__':
    export_data_to_postgres()
