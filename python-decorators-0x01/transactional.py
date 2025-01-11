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

# Decorator to manage database transactions
def transactional(func):
    @functools.wraps(func)
    def wrapper_transactional(conn, *args, **kwargs):
        try:
            # Begin the transaction
            conn.execute("BEGIN")
            # Call the original function
            result = func(conn, *args, **kwargs)
            # Commit the transaction if no error occurs
            conn.commit()
        except Exception as e:
            # Rollback the transaction if an error occurs
            conn.rollback()
            print(f"Transaction rolled back due to error: {e}")
            raise
        return result
    return wrapper_transactional

# Function to update user's email with automatic transaction handling
@with_db_connection
@transactional
def update_user_email(conn, user_id, new_email):
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))

# Update user's email with automatic transaction handling
update_user_email(user_id=77777771, new_email='Crawford_Cartwright@hotmail.com')

