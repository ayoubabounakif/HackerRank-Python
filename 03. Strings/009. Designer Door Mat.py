# Problem: https://www.hackerrank.com/challenges/designer-door-mat/problem

height, length = map(int, input().split())
for i in range(0, height // 2):
    s = '.|.' * (i * 2 + 1)
    print(s.center(length,'-'))
print('WELCOME'.center(length, '-'))
for i in range(height // 2 - 1, -1, -1):
    s = '.|.' * (i * 2 + 1)
    print(s.center(length,'-'))

n, m = map(int,input().split())
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))

# Line 1: Straightforward.
# There are a couple things to notice.
# The first is that each line has a set number of repetitions of '.|.',
# which are centered, and the rest is filled by '-'.
# The second is that the flag is symmetrical, so if you have the top, you have the bottom by reversing it.
# You only need to work on n // 2 
# (n is odd and you need the integer div because the remaining line is the "WELCOME" line).
# Line 2: I generate 2\*i + 1 '.|.', center it, and fill the rest with '-'. That's basically the top part of the output.
# Line 3: put things together. '\n'.join() should be straightforward.
# Then, the sequence of strings to join is the pattern described above, the middle 'WELCOME' line, and the pattern reversed.
