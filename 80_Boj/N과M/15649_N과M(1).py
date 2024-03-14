import sys; sys.stdin = open("input.txt")

N, M = map(int, input().split())

for i in range(1, N+1):
    print(i, end=' ')
    for j in range(1, N+1):
        if i != j:
            print(j)

for m in range(M):
    for i in range(1, N+1):
        pass