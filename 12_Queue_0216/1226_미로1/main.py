T = 10
for t in range(T):
    tc = int(input())
    maze = [input() for _ in range(16)]
    # print(maze)
    di = [-1, 1, 0, 0]  # 상, 하, 좌, 우
    dj = [0, 0, -1, 1]

    q = []
    visited = [[0]*16 for _ in range(16)]
    q.append([1, 1])    # 시작점 인큐
    result = 0

    while q:
        a = q.pop(0)
        for k in range(4):
            ni = a[0] + di[k]
            nj = a[1] + dj[k]
            # print(maze[ni][nj], visited[ni][nj])
            if maze[ni][nj] == '0' and visited[ni][nj] == 0:
                q.append([ni, nj])
                visited[ni][nj] = 1
            if maze[ni][nj] == '3':
                result = 1
                break
    print(f'#{tc} {result}')