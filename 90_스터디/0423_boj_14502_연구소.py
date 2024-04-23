import sys; sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
laboratory = [list(map(int, input().split())) for _ in range(N)]

# 연구소의 크기가 8*8이고 벽을 3개만 세우므로 완전탐색

di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

def virus(arr):
    # 배열을 받아서 바이러스를 퍼뜨리고 안전구역의 개수 반환
    queue = deque()
    visited = [[0]*M for _ in range(N)]
    virus_cnt = 0
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 2:
                queue.append((r, c))
            while queue:
                i, j = queue.popleft()
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if not (0<=ni<N and 0<=nj<M):
                        continue
                    if arr[ni][nj] == 0 and visited[ni][nj] == 0:
                        virus_cnt += 1
                        visited[ni][nj] = 1
                        queue.append((ni, nj))
    cnt = 0
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 0:
                cnt += 1
    return cnt - virus_cnt

# print(virus(laboratory))

# 벽 만들기
def make_wall(x):
    global max_safe
    if x == 3:
        safe = virus(laboratory)
        max_safe = max(max_safe, safe)
        return

    for r in range(N):
        for c in range(M):
            if laboratory[r][c] == 0:
                laboratory[r][c] = 1
                make_wall(x+1)
                laboratory[r][c] = 0


max_safe = 0
make_wall(0)
print(max_safe)



