# Problem: https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

n = int(input())
s = set(map(int, input().split()))
for i in range(int(input())):
    __ = input().split()
    if __[0] == "pop":
        s.pop()
    elif __[0] == "remove":
        s.remove(int(__[1]))
    elif __[0] == "discard":
        s.discard(int(__[1]))
print (sum(s))

