# Problem: https://www.hackerrank.com/challenges/string-validators/problem

if __name__ == '__main__':
    s = input()
    result = ["False", "False", "False", "False", "False"]
    for i in s:
        if i.isalnum():
            result[0] = "True"
        if i.isalpha():
            result[1] = "True"
        if i.isdigit():
            result[2] = "True"
        if i.islower():
            result[3] = "True"
        if i.isupper():
            result[4] = "True"
    print(*result, sep="\n")

if __name__ == '__main__':
    s = input()
    print(any([char.isalnum() for char in s]))
    print(any([char.isalpha() for char in s]))
    print(any([char.isdigit() for char in s]))
    print(any([char.islower() for char in s]))
    print(any([char.isupper() for char in s]))
