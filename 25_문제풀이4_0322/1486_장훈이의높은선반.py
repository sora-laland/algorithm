import sys; sys.stdin = open("input.txt")

T = int(input())
for t in range(T):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
print()