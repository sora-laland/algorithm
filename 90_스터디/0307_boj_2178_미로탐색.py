import sys; sys.stdin = open("input.txt")
input = sys.stdin.readline
from collections import deque


N, M = map(int, input().split())
maze = [input() for _ in range(N)]

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
q = deque()
visited = [[0]*M for _ in range(N)]

q.append((0, 0))
visited[0][0] = 1  # 방문표시
while q:
    i, j = q.popleft()
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0<=ni<N and 0<=nj<M:
            if maze[ni][nj] == '1' and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = (visited[i][j] + 1)
                # 지나온 길에+1 해서 대체해주기

print(visited[N-1][M-1])