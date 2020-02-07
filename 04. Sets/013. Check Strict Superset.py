# Problem: https://www.hackerrank.com/challenges/py-check-strict-superset/problem

set_a = set(input().split())
print (all(set_a >= set(input().split()) for x in range(int(input()))))

