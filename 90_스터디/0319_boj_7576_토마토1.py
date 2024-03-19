import sys; sys.stdin = open("input.txt")
from collections import deque

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

M, N = map(int, input().split())
tomatoes = [list(map(int, input().split())) for _ in range(N)]
q = deque()

for r in range(N):
    for c in range(M):
        if tomatoes[r][c] == 1:
            q.append((r, c))

while q:
    i, j = q.popleft()

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if ni < 0 or ni >= N or nj < 0 or nj >= M:
            continue
        if tomatoes[ni][nj] == 0:
            q.append((ni, nj))
            tomatoes[ni][nj] = tomatoes[i][j] + 1

ans = -1
max_val = 0
for row in tomatoes:
    if 0 in row:
        break
    if max(row) > max_val:
        max_val = max(row)
else:
    ans = max_val -1
print(ans)