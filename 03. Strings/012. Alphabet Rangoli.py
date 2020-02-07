# Problem: https://www.hackerrank.com/challenges/alphabet-rangoli/problem

if __name__ == '__main__':
    import string
    n = int(input())
    alpha = string.ascii_lowercase
    list_ = []
    for i in range (n):
        s = '-'.join(alpha[i:n])
        list_.append(s[::-1]+s[1:])
    width = len(list_[0])
    for i in range(n-1, 0, -1):
        print(list_[i].center(width, "-"))
    for i in range(n):
        print(list_[i].center(width, "-"))

import string
size = int(input())
alphabet = string.ascii_lowercase
for i in range(size - 1, 0, -1):
    row = ["-"] * (size * 2 - 1)
    for j in range(0, size - i):
        row[size - 1 - j] = alphabet[j + i]
        row[size - 1 + j] = alphabet[j + i]
    print("-".join(row))
for i in range(0, size):
    row = ["-"] * (size * 2 - 1)
    for j in range(0, size - i):
        row[size - 1 - j] = alphabet[j + i]
        row[size - 1 + j] = alphabet[j + i]
    print("-".join(row))
