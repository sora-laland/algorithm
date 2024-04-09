import sys; sys.stdin = open("input.txt")
from collections import deque


def bfs(r, c):
    queue = deque()
    queue.append((r, c))
    visited[r][c] = 1
    while queue:
        i, j = queue.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if not (0<=ni<N and 0<=nj<M):
                continue
            if arr[ni][nj] == 1 and visited[ni][nj] == 0:
                queue.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1


T = int(input())
for t in range(T):
    M, N, K = map(int, input().split())
    arr = [[0]*M for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, input().split())
        arr[Y][X] = 1
    # print(arr)
    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]
    visited = [[0]*M for _ in range(N)]

    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and visited[i][j] == 0:
                bfs(i, j)
                cnt += 1

    print(cnt)