import sys; sys.stdin = open('input.txt')
from collections import deque
from itertools import combinations_with_replacement
from copy import deepcopy


di = [-1, 1, 0, 0]
dj = [0, 0, 1, -1]

def pang(r, c, arr):
    queue = deque()
    queue.append((r, c))
    while queue:
        i, j = queue.popleft()
        block = arr[i][j]
        arr[i][j] = 0
        for x in range(1, block):
            for k in range(4):
                ni = i + x * di[k]
                nj = j + x * dj[k]
                if 0<=ni<H and 0<=nj<W:
                    queue.append((ni, nj))
    return arr


def falling(arr):
    all_0 = 0
    for j in range(W):
        cnt_0 = 0
        for i in range(H-1, -1, -1):
            if arr[i][j] == 0:
                cnt_0 += 1
            if arr[i][j]:
                if cnt_0:
                    arr[i+cnt_0][j] = arr[i][j]
                    arr[i][j] = 0
        all_0 += cnt_0
    return all_0


def find_top_(j, arr):
    for i in range(H):
        if arr[i][j]:
            return i, j
    else:
        return

T = int(input())
for t in range(T):
    N, W, H = map(int, input().split())
    plate = [list(map(int, input().split())) for _ in range(H)]


    combis = list(combinations_with_replacement(range(W), N))
    # W**N 만큼 반복
    max_0 = 0
    for combi in combis:
        arr = deepcopy(plate)
        # N 만큼 반복
        for j in combi:
            top = find_top_(j, arr)
            if top == None:
                continue
            r, c = top
            pang(r, c, arr)
            cnt = falling(arr)
        max_0 = max(max_0, cnt)

    min_block = W*H - max_0
    print(f'#{t+1} {min_block}')
