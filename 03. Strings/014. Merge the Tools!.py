# Problem: https://www.hackerrank.com/challenges/merge-the-tools/problem

import textwrap
from collections import OrderedDict
def merge_the_tools(string, k):
    list_ = textwrap.wrap(string, k)
    list__ = []
    for i in list_:
        list__.append(''.join(OrderedDict.fromkeys(i)))
    for i in list__:
        print (i)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
