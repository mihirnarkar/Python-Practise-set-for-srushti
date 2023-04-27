'''
Q3) Given a maximum of four digit to the base 17(10-A, 11-B, 12-C, 13-D, ... 16-G) as input. Output its decimal values.   
Cases: 
input: 1A , output: 27
'''

# Define a dictionary to map each letter to its corresponding value
base17_values = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16
}

# Get user input
base17_num = input("Enter a maximum of four digit to the base 17: ")

# Convert the base 17 number to decimal
decimal_num = 0
for i in range(len(base17_num)):
    digit = base17_num[-i-1] # Get the i-th digit from the right
    value = base17_values[digit]
    decimal_num += value * (17 ** i)

# Print the decimal equivalent
print(f"The decimal equivalent of {base17_num} is {decimal_num}.")
