import sys; sys.stdin = open("input.txt")

N, M = map(int, input().split())
path = []
visited = [0] * (N+1)


def comb(x):
    if x == M:
        print(*path)
        return

    for i in range(1, N+1):
        if i in path:
            continue
        if visited[i] == 1:
            continue
        path.append(i)
        visited[i] = 1
        comb(x+1)
        path.pop()


comb(0)