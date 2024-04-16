import sys; sys.stdin = open('input.txt')
from collections import deque

N, W, H = map(int, input().split())
plate = [list(map(int, input().split())) for _ in range(H)]

di = [-1, 1, 0, 0]
dj = [0, 0, 1, -1]

def pang(r, c):
    queue = deque()
    queue.append((r, c))
    while queue:
        i, j = queue.popleft()
        block = plate[i][j]
        plate[i][j] = 0
        for x in range(1, block):
            for k in range(4):
                ni = i + x * di[k]
                nj = j + x * dj[k]
                if 0<=ni<H and 0<=nj<W:
                    queue.append((ni, nj))


pang(1, 2)
print(plate)

pang(2, 2)
print(plate)
