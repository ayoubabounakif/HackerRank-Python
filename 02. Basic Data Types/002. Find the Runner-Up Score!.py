# Problem: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    arr = sorted(set(list(map(int, input().split()))))
    print (arr[-2])
