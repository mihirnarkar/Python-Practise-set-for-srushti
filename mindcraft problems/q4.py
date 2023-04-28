'''Q.4) Given a maximum of 100 digits numbers as input, find the difference between the sum of odd and even position digits

Test cases:
Case 1: 
-> Input : 4567
-> Output : 2

Case 2:
-> Input : 5476
-> Output : 2

Case 3:
-> Input : 9834698765123
-> Output : 1

Explanation: For Test case 1
-> Odd position are 4 and 6 as they are pos: 1 and pos: 3, both have sum 10. Similarly 5 and 7 as they are 
pos: 2 and pos: 4
Sum of odd : 10
sum of even : 12
Diff : 12 - 10 = 2
'''


# Solution:-


def difference_odd_even_digits(input_string):
    odd_sum = 0
    even_sum = 0
    for i in range(len(input_string)):
        if i % 2 == 0:
            even_sum += int(input_string[i])
        else:
            odd_sum += int(input_string[i])
    return abs(odd_sum - even_sum)
    # 'abs' return the absolute value that means it will not return negative value


print(f"Input: 4567, output: {difference_odd_even_digits('4567')}\n")

print(f"Input: 5476, output: {difference_odd_even_digits('5476')}\n")

print(f"Input: 9834698765123, output: {difference_odd_even_digits('9834698765123')}")






