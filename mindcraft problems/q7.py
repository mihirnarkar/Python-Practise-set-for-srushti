'''
Q.7) Find the nth term of the series

series: 1,1,2,3,4,9,8,27,16,81,32,243,64,729,128,2187

This series is a mixture of 2 series - all the odd term in this series from a geometric series and all the even terms from another geometric series. Write a program to find Nth term in the series.

condition:
1) The value of N is a positive integer that should be read from stdin
2) The Nth term that is calculated by the program should be written in stdout
3) Other than value of nth term, no other character/string or message should be wriiten in stdout
4) For example: If N = 16, the 16th term in the series is 2187 should be printed to stdout
5) You can assume n will not exceed 30

Test case 1:
Input: 16
Output: 2187

Test case 2:
Input: 13
Output: 64
'''


'''
My output
'''
# series = [1,1,2,3,4,9,8,27,16,81,32,243,64,729,128,2187]

# # Test case 1:
# user1 = 16
# user2 = 10
# if user1<=len(series) and user2<=len(series):
#     print(f"Input: {user1}, Output: {str(series[user1-1])}")
#     print(f"Input: {user2}, Output: {str(series[user2-1])}")
# else:
#     print("Series exceeded")


'''
Open ai output
'''

n = int(input())
if n % 2 == 0:
    # Even term
    print(str(3 ** ((n // 2) - 1)))
else:
    # Odd term
    print(str(2 ** (n // 2)))
