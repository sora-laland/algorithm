import sys; sys.stdin = open("input.txt")

N = int(input())
print(' ' * (N-1) + '*')
for i in range(N-1):
    print(' ' * (N-2-i) + '*', end='')
    print(' ' * (2*i + 1) + '*')
