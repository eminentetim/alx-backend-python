# Define the firstn function using a generator
def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1

# Call the firstn function and print the numbers
def main():
    n = 10  # Change this value to generate a different number of elements
    for number in firstn(n):
        print(number)

# Execute the main function
if __name__ == "__main__":
    main()

