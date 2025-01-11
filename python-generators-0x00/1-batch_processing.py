import mysql.connector

# Generator function to fetch rows in batches from the user_data table

def stream_users_in_batches(batch_size):
    connection = mysql.connector.connect(
        host="localhost",
        user="eminent",
        password="EMINENT1456@sql",
        database="ALX_prodev"
    )
    cursor = connection.cursor(dictionary=True)

    # Execute the query
    cursor.execute("SELECT * FROM user_data")

    # Fetch rows in batches
    while True:
        rows = cursor.fetchmany(batch_size)
        if not rows:
            break
        yield rows

    cursor.close()
    connection.close()

# Function to process each batch to filter users over the age of 25

def batch_processing(batch_size=50):
    """
    Process users in batches, filtering users over 25 years old
    """
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user['age'] > 25:
                print(user)
