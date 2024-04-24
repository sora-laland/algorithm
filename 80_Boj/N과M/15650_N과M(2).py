import sys; sys.stdin = open("input.txt")

N, M = map(int, input().split())
path = []


def comb(x):
    if x == M:
        print(*path)
        return

    for i in range(1, N+1):
        # 직전에 뽑은 요소가 지금보다 크면 continue
        if len(path) >= 1 and path[-1] >= i:
            continue
        path.append(i)
        comb(x+1)
        path.pop()

comb(0)