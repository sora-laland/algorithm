import sys; sys.stdin = open('input.txt')
from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# print(arr)
visited = [[0]*M for _ in range(N)]
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]


def bfs(r, c):
    q = deque()
    q.append((r, c))
    visited[r][c] = 1
    cnt_ice = 0
    while q:
        i, j = q.popleft()
        cnt_ice += 1
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<N and 0<=nj<N:
                if visited[ni][nj] == 0 and arr[ni][nj]:
                    q.append((ni, nj))
                    visited[ni][nj] = 1
    return cnt_ice


def ice():
    arr_copy = [row[:] for row in arr]
    for i in range(N):
        for j in range(M):
            melt_cnt = 0
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    if arr[ni][nj] == 0:
                        melt_cnt += 1
            arr_copy[i][j] = max((arr[i][j] - melt_cnt), 0)
    return arr_copy


print(bfs(1, 1))


result = 0
while True:
    visited = [[0] * M for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0 and arr[i][j]:
                bfs(i, j)
                cnt += 1
                print(result, cnt)
    if cnt >= 2:
        break
    elif cnt < 2:
        result += 1
    arr = ice()

print(result)