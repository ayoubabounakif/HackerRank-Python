# Problem: https://www.hackerrank.com/challenges/py-check-subset/problem

for i in range(int(input())):
    _, a = int(input()), set(map(int, input().split()))
    _, b = int(input()), set(map(int, input().split()))
    print (a.issubset(b))
    print (b.issubset(a))
