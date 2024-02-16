from collections import deque

T = int(input())
for t in range(T):
    N = int(input())
    visited = [[0] * N for _ in range(N)]
    maze = [input() for _ in range(N)]
    di = [-1, 1, 0, 0]  # 상, 하, 좌, 우
    dj = [0, 0, -1, 1]
    x, y = 0, 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                x, y = i, j
    q = deque()
    q.append((x, y, 0))     # 뎁스 같이 붙여줌
    ans = 0

    while q:
        i, j, k = q.popleft()
        if maze[i][j] == '3':
            ans = k - 1  # 도착점이 도착하는 이동은 빼줌
            q.clear()
            break
        visited[i][j] = 1   # 방문체크
        for ii, jj in zip(di, dj):
            ni = i + ii
            nj = j + jj
            if not (0<=ni<N):
                continue
            if not (0<=nj<N):
                continue
            if visited[ni][nj]:
                continue
            # 벽이 '1'
            if maze[ni][nj] == '1':
                continue
            q.append((ni, nj, k+1))  # 뎁스에 1 추가

    print(f'#{t+1}', end=' ')
    print(ans)
