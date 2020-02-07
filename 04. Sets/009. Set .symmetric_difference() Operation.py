# Problem: https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

n_engnp, n__ = int(input()), set(input().split())
b_frnp, b__= int(input()), set(input().split())
print(len(n__.symmetric_difference(b__)))
