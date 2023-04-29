# Problem : Find the cube of a value which is passed inside the function(named function as cube) pass the values to the function and calculate the cube.


# For reference i have solved (square) this problem, check it out:

def square(value):
    square_value = value * value
    return square_value

user_value = 9
print(f"Square value of {user_value} = {square(user_value)}")
#                           \                  \
#                     print user value     pass the user value to the function
#                                            Its will print the square value


# Similarly solve this for cube