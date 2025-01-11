import time
import sqlite3
import functools

# Dictionary to store cached query results
query_cache = {}

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

# Decorator to cache query results based on the SQL query string
def cache_query(func):
    @functools.wraps(func)
    def wrapper_cache_query(conn, query, *args, **kwargs):
        # Check if the query result is already cached
        if query in query_cache:
            print("Using cached result")
            return query_cache[query]

        # If not cached, execute the query and cache the result
        result = func(conn, query, *args, **kwargs)
        query_cache[query] = result
        print("Caching new result")
        return result
    return wrapper_cache_query

# Function to fetch users with caching
@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

# First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")
print(users)

# Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")
print(users_again)

