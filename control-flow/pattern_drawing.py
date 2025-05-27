# pattern_drawing.py

# Prompt user for a positive integer
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop to iterate through each row
while row < size:
    # Use a for loop to print asterisks in one row
    for _ in range(size):
        print("*", end="")
    print()  # Move to the next line after one row is printed
    row += 1