import sys; sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 연구소의 크기가 8*8이고 벽을 3개만 세우므로 완전탐색

di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

def virus():
    queue = deque()
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
                    if arr[ni][nj] == 0:
                        arr[ni][nj] = 2
                        queue.append((ni, nj))
    cnt = 0
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 0:
                cnt += 1
    return cnt



# print(virus())

# 벽 만들기
def make_wall(x):
    if x == 3:
        return

    for r in range(N):
        for c in range(M):
            if arr[r][c] == 0:
                arr[r][c] = 1
                make_wall(x+1)
                print(virus())
                arr[r][c] = 0


make_wall()
print(arr)

