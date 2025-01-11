import mysql.connector

# Function to connect to the ALX_prodev database in MySQL
def connect_to_prodev():
    return mysql.connector.connect(
        host="localhost",
        user="eminent",
        password="EMINENT1456@sql",
        database="ALX_prodev"
    )

# Generator function to yield user ages one by one
def stream_user_ages():
    connection = connect_to_prodev()
    cursor = connection.cursor()
    cursor.execute("SELECT age FROM user_data")

    for row in cursor:
        yield row[0]

    cursor.close()
    connection.close()

# Function to calculate the average age using the generator
def calculate_average_age():
    total_age = 0
    count = 0

    for age in stream_user_ages():
        total_age += age
        count += 1

    if count == 0:
        return 0  # Handle the case where there are no users

    average_age = total_age / count
    return average_age

# Main function to print the average age of users
def main():
    average_age = calculate_average_age()
    print(f"Average age of users: {average_age:.2f}")
if __name__ == "__main__":
    main()

