import sys; sys.stdin=open('input.txt')
input = sys.stdin.readline
from collections import deque

N = int(input())
graph = [input().rstrip() for _ in range(N)]
visited = [[0] * N for _ in range(N)]
w_visited = [[0] * N for _ in range(N)]


di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
cnt = 0
w_cnt = 0


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
            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                continue
            if visited[ni][nj] == 0 and graph[ni][nj] == graph[i][j]:
                queue.append((ni, nj))
                visited[ni][nj] = 1
    cnt += 1
    # print(cnt)

def w_bfs(i, j):
    global w_cnt
    queue = deque()
    queue.append((i, j))
    w_visited[i][j] = 1
    while queue:
        v = queue.popleft()
        for k in range(4):
            ni = v[0] + di[k]
            nj = v[1] + dj[k]
            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                continue
            if w_visited[ni][nj] == 0:
                if graph[ni][nj] == 'B' and graph[i][j] == 'B':
                    queue.append((ni, nj))
                    w_visited[ni][nj] = 1
                if graph[ni][nj] in 'GR' and graph[i][j] in 'GR':
                    queue.append((ni, nj))
                    w_visited[ni][nj] = 1
    w_cnt += 1
    # print(w_cnt)

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            bfs(i, j)
        if w_visited[i][j] == 0:
            w_bfs(i, j)

print(cnt, w_cnt)

