import sys; sys.stdin = open("input.txt")

from collections import deque

T = int(input())
for t in range(T):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    number = [
        [],
        [1, 1, 1, 1],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 1, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 1, 1],
        [1, 0, 0, 1]
    ]

    dir_idx = [[1, 2, 4, 7], [1, 3, 4, 5], [1, 3, 6, 7], [1, 2, 5, 6]]

    # 상 우 좌 하
    di = [-1, 0, 0, 1]
    dj = [0, 1, -1, 0]

    queue = deque()
    visited = [[0]*M for _ in range(N)]
    # 시작점 인큐
    queue.append((R, C))
    visited[R][C] = 1
    cnt = 1
    while queue:
        i, j = queue.popleft()
        if visited[i][j] == L:
            break

        # 위가 뚫려 있다면 위쪽을 확인 해봐야 한다
        for k in range(4):
            if arr[i][j] in dir_idx[k]:
                dir = k
                ni = i + di[dir]
                nj = j + dj[dir]
                if ni < 0 or ni >= N or nj < 0 or nj >= M:
                    continue
                if visited[ni][nj] != 0:
                    continue
                if arr[ni][nj] in dir_idx[3-dir]:
                    queue.append((ni, nj))
                    visited[ni][nj] = visited[i][j] + 1
                    cnt += 1

    print(f'#{t+1} {cnt}')