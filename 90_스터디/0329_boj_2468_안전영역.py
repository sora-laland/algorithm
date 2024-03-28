import sys; sys.stdin = open('input.txt')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]


def dfs(i, j):
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if not ((0<=ni<N) and (0<=nj<N)):
            continue
        if arr[ni][nj] <= depth:
            continue
        if visited[ni][nj]:
            continue

        visited[ni][nj] = visited[i][j]+1
        dfs(ni, nj)


def count_1():
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 1:
                cnt += 1
    return cnt


max_cnt = 0
for depth in range(0, 101):
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] > depth and visited[i][j] == 0:
                visited[i][j] = 1
                dfs(i, j)
    cnt = count_1()
    max_cnt = max(max_cnt, cnt)
    if cnt == 0:
        break

print(max_cnt)