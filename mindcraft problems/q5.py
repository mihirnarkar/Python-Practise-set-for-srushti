'''
Q.5) Program to check if a year is leap or not

-> Explanation:-
A leap year is a year that is evenly divisible by 4, except for years that are evenly divisible by 100. However, years that are evenly divisible by 400 are also leap years.

So, the conditions for a leap year are:

1) If the year is evenly divisible by 4, it is a potential leap year.
2) If the year is evenly divisible by 100, it is not a leap year, unless:
3) The year is also evenly divisible by 400, in which case it is a leap year.

For example, 2020 is a leap year because it is divisible by 4, but not by 100. 1900 is not a leap year because it is divisible by both 4 and 100, but not by 400. 2000 is a leap year because it is divisible by both 4 and 400.
'''

# Solution :-
def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


year = 2000
print(f"{year} -> {is_leap_year(year)}\n")

year = 2010
print(f"{year} -> {is_leap_year(year)}\n")

year = 1900
print(f"{year} -> {is_leap_year(year)}\n")

year = 2024
print(f"{year} -> {is_leap_year(year)}\n")
