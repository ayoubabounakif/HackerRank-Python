# Problem: https://www.hackerrank.com/challenges/py-set-mutations/problem

int_a, set_a = int(input()), set(map(int, input().split()))
for i in range(int(input())):
    command = input().split()[0]
    set__ = set(map(int, input().split()))
    if command == 'intersection_update':
        set_a.intersection_update(set__)
    if command == 'update':
        set_a.update(set__)
    if command == 'symmetric_difference_update':
        set_a.symmetric_difference_update(set__)
    if command == 'difference_update':
        set_a.difference_update(set__)
print (sum(set_a))
