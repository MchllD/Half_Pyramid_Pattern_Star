# Exercise 14: Print a downward Half-Pyramid Pattern of Star (asterisk)

# pseudocode

# function to print a downward half pyramid
# create outer loop for rows (starting from the given number of rows and decreasing)
# Inner loop for printing '*' based on the current row value
# Move to the next line after printing '*' for the current row
# Set the number of rows for the downward half pyramid

# ------------------------------- pseudocode ---------------------------------------------------


# function to print a downward half pyramid
def print_downward_half_pyramid(rows):
    # create outer loop for rows (starting from the given number of rows and decreasing)
    for i in range(rows, 0, -1):
        # Inner loop for printing '*' based on the current row value
        for j in range(i):
            print("*", end=" ")
        # Move to the next line after printing '*' for the current row
        print()
        
# Set the number of rows for the downward half-pyramid
num_rows = 5

print_downward_half_pyramid(num_rows)