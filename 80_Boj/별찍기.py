import sys; sys.stdin = open("input.txt")

N = int(input())
for i in range(1, N):
    print('*' * i, end='')
    print(' ' * (2*(N-i)), end='')
    print('*' * i)
for i in range(N-1, -1, -1):
    print('*' * (i+1), end='')
    print(' ' * (2*(N-i-1)), end='')
    print('*' * (i+1))
