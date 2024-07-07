import sys; sys.stdin=open('input.txt')
input = sys.stdin.readline
from collections import deque


def bfs(i, j):
    global cnt
    queue = deque()
    queue.append((i, j))
    visited[i][j] = 1
    while queue:
        v = queue.popleft()
        for k in range(4):
            ni = v[0] + di[k]
            nj = v[1] + dj[k]
            if ni < 0 or ni >= N or nj < 0 or nj >= M:
                continue
            if visited[ni][nj] == 0 and graph[ni][nj]:
                queue.append((ni, nj))
                visited[ni][nj] = 1
    cnt += 1


def one_year():
    minus_arr = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                continue
            zero_cnt = 0
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if ni < 0 or ni >= N or nj < 0 or nj >= M:
                    continue
                if graph[ni][nj] == 0:
                    zero_cnt += 1
            minus_arr[i][j] = zero_cnt
    for i in range(N):
        for j in range(M):
            graph[i][j] -= minus_arr[i][j]
            graph[i][j] = max(graph[i][j], 0)


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
year_cnt = 0
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]


while True:
    if graph == [[0] * M for _ in range(N)]:
        break
    cnt = 0
    visited = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0 and visited[i][j] == 0:
                bfs(i, j)
    if cnt >= 2:
        break
    one_year()
    year_cnt += 1


if cnt >= 2:
    print(year_cnt)
else:
    print(0)



