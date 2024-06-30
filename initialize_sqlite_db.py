import sqlite3

def initialize_db():
    conn = sqlite3.connect('funds.db')
    cursor = conn.cursor()
    
    # Create the funds table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS funds (
            fund_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            manager_name TEXT,
            description TEXT,
            nav REAL,
            date_of_creation TEXT,
            performance REAL
        )
    ''')
    
    # Insert some test data
    cursor.execute('''
        INSERT INTO funds (name, manager_name, description, nav, date_of_creation, performance)
        VALUES
        ('Alpha Fund', 'John Doe', 'High-risk fund', 1000000, '2024-01-01', 10.5),
        ('Beta Fund', 'Jane Doe', 'Stable fund', 500000, '2024-06-27', 3.0)
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    initialize_db()
