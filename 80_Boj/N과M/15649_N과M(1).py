import sys; sys.stdin = open("input.txt")

N, M = map(int, input().split())
arr = list(range(N+1))
path = []
def perm(x):
    if x == M:
        print(*path)
        return

    for i in range(1, N+1):
        if i in path:
            continue
        path.append(i)
        perm(x+1)
        path.pop()

perm(0)