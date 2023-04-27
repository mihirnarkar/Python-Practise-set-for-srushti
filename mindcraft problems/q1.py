'''
Q.1) WAP to either print the series or print a specific number from the series as per user input. Eg input: n=6. O/P: 2   
Consider The series:  0,0,2,1,4,2,6,3,8,4,10,5,12,6,14,7,16,8
'''

'''
Solution:-
'''

# Define the series:-
series = [0,0,2,1,4,2,6,3,8,4,10,5,12,6,14,7,16,8]

# User input:-
user = int(input("Enter a number to print from the series: "))

# Check if user input is within a range
if (user<1 or user>len(series)):
    print("Invalid input! Plzz enter number within series")
else:
    # Print the entire series if n = -1
    if(user == -1):
        print(series)

    # Otherwise, print the nth number in the series
    else:
        print(series[user-1])
