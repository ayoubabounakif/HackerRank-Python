# Problem: https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/probleimport itertools

from itertools import combinations_with_replacement

s = input().split()
str_, num_ = sorted(s[0]), int(s[1])
print (*list(map(''.join, combinations_with_replacement(str_, num_))), sep = '\n')
