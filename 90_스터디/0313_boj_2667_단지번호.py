import sys; sys.stdin = open("input.txt")
from collections import deque

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
# print(arr)
visited = [[0]*N for _ in range(N)]
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]


def bfs(i, j):
    q = deque()
    # 첫 좌표 인큐(arr[i][j]==1 이어야 함)
    q.append((i, j))
    visited[i][j] = 1
    cnt = 1     # 단지 내 집의 수
    while q:
        v = q.popleft()
        for k in range(4):
            ni = v[0] + di[k]
            nj = v[1] + dj[k]
            if 0<=ni<N and 0<=nj<N:
                if visited[ni][nj] == 0 and arr[ni][nj]:
                    q.append((ni, nj))
                    visited[ni][nj] = 1
                    cnt += 1
    return cnt


lst = []
for i in range(N):
    for j in range(N):
        if arr[i][j] and visited[i][j] == 0:
            lst.append(bfs(i, j))
lst.sort()

print(len(lst))
print(*lst, sep='\n')