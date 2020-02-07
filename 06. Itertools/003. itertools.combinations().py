# Problem: https://www.hackerrank.com/challenges/itertools-combinations

from itertools import combinations

s = input().split()
str_, num_ = sorted(s[0]), int(s[1])
for i in range(1, num_+1):
    print (*list(map(''.join,combinations(str_, i))), sep='\n')

