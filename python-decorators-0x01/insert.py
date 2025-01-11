import sqlite3

# Create a connection to the database
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create the users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL
)
""")

# Insert sample data into the users table
sample_data = [
    (1, 'John Doe', 'john.doe@example.com'),
    (2, 'Jane Smith', 'jane.smith@example.com'),
    (3, 'Emily Jones', 'emily.jones@example.com')
]
cursor.executemany("INSERT INTO users (id, name, email) VALUES (?, ?, ?)", sample_data)
conn.commit()
conn.close()

