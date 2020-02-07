# Problem: https://www.hackerrank.com/challenges/itertools-permutations/problem

from itertools import permutations

s = input().split()
str_, num_ = sorted(s[0]), int(s[1])

print (*list(map(''.join, permutations(str_, num_))), sep='\n')
