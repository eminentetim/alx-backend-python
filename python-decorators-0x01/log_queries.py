import sqlite3
import functools
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Decorator to log SQL queries
def log_queries(func):
    @functools.wraps(func)
    def wrapper_log_queries(*args, **kwargs):
        query = kwargs.get('query') or args[0]
        logging.info(f"Executing query: {query}")
        return func(*args, **kwargs)
    return wrapper_log_queries

# Function to fetch all users with logging
@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

# Fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")

# Print the fetched users
for user in users:
    print(user)

