import time
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

# Decorator to retry the function if it raises an exception
def retry_on_failure(retries=3, delay=2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper_retry(*args, **kwargs):
            num_attempts = 0
            while num_attempts < retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    num_attempts += 1
                    print(f"Attempt {num_attempts} failed: {e}. Retrying in {delay} seconds...")
                    time.sleep(delay)
            # If all attempts fail, raise the last exception
            raise e
        return wrapper_retry
    return decorator

# Function to fetch users with automatic retry on failure
@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

# Attempt to fetch users with automatic retry on failure
users = fetch_users_with_retry()
print(users)

