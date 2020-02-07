# Problem: https://www.hackerrank.com/challenges/write-a-function/problem

def is_leap(year):
    leap = False
    if 1900 <= year <= 10**5:
        if year % 4 == 0 and year % 100 != 0:
            return True
        elif year % 400 == 0:
            return True
    
    return leap

year = int(input())
print(is_leap(year))

# def is_leap(y):
#     return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)
