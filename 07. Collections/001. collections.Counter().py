# Problem: https://www.hackerrank.com/challenges/collections-counter/problem

number_of_shoes = int(input())
sizes_in_stock = collections.Counter(map(int, input().split()))
money_earned = 0
for _ in range(int(input())):
    size, price = map(int, input().split())
    
