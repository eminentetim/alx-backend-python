import mysql.connector

# Function to connect to the ALX_prodev database in MySQL
def connect_to_prodev():
    return mysql.connector.connect(
        host="localhost",
        user="eminent",
        password="EMINENT1456@sql",
        database="ALX_prodev"
    )

# Function to fetch a specific page of users from the database
def paginate_users(connection, page_size, offset):
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM user_data LIMIT %s OFFSET %s"
    cursor.execute(query, (page_size, offset))
    rows = cursor.fetchall()
    cursor.close()
    return rows

# Generator function to lazily load each page of users
def lazy_paginate(page_size):
    connection = connect_to_prodev()
    offset = 0

    while True:
        users = paginate_users(connection, page_size, offset)
        if not users:
            break
        yield users
        offset += page_size

    connection.close()

# Example usage of the generator function
if __name__ == "__main__":
    page_size = 5  # Set the page size

    # Process and print each page
    for page in lazy_paginate(page_size):
        print("Fetched page:")
        for user in page:
            print(user)

