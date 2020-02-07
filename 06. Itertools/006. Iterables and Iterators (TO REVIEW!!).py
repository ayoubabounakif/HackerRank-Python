# Problem: https://www.hackerrank.com/challenges/iterables-and-iterators/problem

############### NOT UNDERSTOOD!! TO REVIEW!! ##################

from itertools import combinations

"""n, number, k = int(input()), input().split(' '), int(input())
num, den = 0, 0
for i in combinations(number, k):
    den += 1
    if 'a' in i:
        num += 1

print (float(num)/den)


n, number, k = int(input()), input().split(' '), int(input())
found = ['a' in i for i in combinations(number, k)]
print (float(sum(found)/len(found)))"""

n, alphalist, k = int(input()), input().split(), int(input())
count = 0
comb = list(combinations(n, k))
for i in comb:
    if index in i:
        count+=1

print (float(count)/len(comb))

