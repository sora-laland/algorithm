import sys; sys.stdin = open("input.txt")
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

path = []
def perm(x):
    if x == M:
        print(*path)
        return

    for i in arr:
        if i in path:
            continue
        path.append(i)
        perm(x+1)
        path.pop()

perm(0)