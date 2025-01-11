import sqlite3
import functools

# Decorator to automatically handle opening and closing database connections
def with_db_connection(func):
    @functools.wraps(func)
    def wrapper_db_connection(*args, **kwargs):
        # Open the database connection
        conn = sqlite3.connect('users.db')
        try:
            # Call the original function with the connection object
            result = func(conn, *args, **kwargs)
        finally:
            # Close the database connection
            conn.close()
        return result
    return wrapper_db_connection

# Function to get a user by ID with automatic connection handling
@with_db_connection
def get_user_by_id(conn, user_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()

# Fetch user by ID with automatic connection handling
user = get_user_by_id(user_id=1)
print(user)

