# Problem: https://www.hackerrank.com/challenges/symmetric-difference/problem

int_m, m_ints = int(input()), set(map(int, input().split()))
int_n, n_ints = int(input()), set(map(int, input().split()))
print (*sorted(m_ints.symmetric_difference(n_ints)), sep = '\n')
