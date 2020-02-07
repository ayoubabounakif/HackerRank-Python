# Problem: https://www.hackerrank.com/challenges/no-idea/problem

ask_user = input()
array = input().split()
set_a = set(input().split())
set_b = set(input().split())
happiness = 0
for i in array:
    if i in set_a:
        happiness += 1
    elif i in set_b:
        happiness -= 1
print (happiness)
