import sys; sys.stdin = open("input.txt")
from collections import deque
import sys
input = sys.stdin.readline

di = [1, -1, 0, 0, 0, 0]
dj = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

M, N, H = map(int, input().split())
tomatoes = []
for _ in range(H):
    box = [list(map(int, input().split())) for _ in range(N)]
    tomatoes.append(box)

q = deque()

for h in range(H):
    for r in range(N):
        for c in range(M):
            if tomatoes[h][r][c] == 1:
                q.append((h, r, c))

while q:
    z, i, j = q.popleft()

    for k in range(6):
        nz = z + dz[k]
        ni = i + di[k]
        nj = j + dj[k]
        if ni < 0 or ni >= N or nj < 0 or nj >= M or nz < 0 or nz >= H:
            continue
        if tomatoes[nz][ni][nj] == 0:
            q.append((nz, ni, nj))
            tomatoes[nz][ni][nj] = tomatoes[z][i][j] + 1


# print(tomatoes)

max_v = 0
for h in range(H):
    for n in range(N):
        for m in range(M):
            if tomatoes[h][n][m] == 0:
                print(-1)
                exit()
            if max_v < tomatoes[h][n][m]:
                max_v = tomatoes[h][n][m]
print(max_v - 1)

# ans = -1
# max_val = 0
# flag = 0
# for box in tomatoes:
#     if flag:
#         break
#     for row in box:
#         if 0 in row:
#             flag = 1
#             break
#         if max(row) > max_val:
#             max_val = max(row)
# else:
#     ans = max_val - 1
# print(ans)