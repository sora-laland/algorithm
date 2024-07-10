import sys; sys.stdin=open('input.txt')
input = sys.stdin.readline
from collections import deque

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
max_move = 0

def bfs(r, c):
    visited = [[0]*n for _ in range(n)]
    queue = deque()
    queue.append((r, c))
    visited[r][c] = 1
    max_val = 0
    while queue:
        i, j = queue.popleft()
        for k in range(n):
            ni = i + di[k]
            nj = j + dj[k]
            if ni < 0 or ni >= n or nj < 0 or nj >= n:
                continue
            if visited[ni][nj] == 0 and arr[i][j] < arr[ni][nj]:
                queue.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
                max_val = max(max_val, visited[ni][nj])
    return max_val
    # print(max_val)

for r in range(n):
    for c in range(n):
        max_move = max(max_move, bfs(r, c))
print(max_move)
