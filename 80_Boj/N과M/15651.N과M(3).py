import sys; sys.stdin = open("input.txt")

N, M = map(int, input().split())
arr = list(range(N+1))
path = []
def perm_duple(x):
    if x == M:
        print(*path)
        return

    for i in range(1, N+1):
        path.append(i)
        perm_duple(x+1)
        path.pop()

perm_duple(0)