# Problem: https://www.hackerrank.com/challenges/py-the-captains-room/problsize
# TO REVIEW!!

k, arr = int(input()), list(map(int, input().split()))
my_set = set(arr)
print (((sum(my_set)*k)-(sum(arr))) // (k-1))

