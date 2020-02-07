# Problem: https://www.hackerrank.com/challenges/compress-the-string/problem

# Solution n°1:

from itertools import groupby

string = input()
print (*[(len(list(c)), int(k)) for k, c in groupby(string)])

# I'm unpacking the list comprehension and printing each element of it
# The list is build of elements of (len(list(c), int(k))
# len(list(c)) is simply the number of occurences of a character c returned by the groupby function
# int(k) is just the key value, the character itself


# Solution n°2:

from itertools import groupby

for key, c in groupby(map(int, list(input()))):
    print (tuple([len(list(c)), key]),end=' ')
