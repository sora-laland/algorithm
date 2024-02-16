T = int(input())
for t in range(T):
    N = int(input())
    maze = [input() for _ in range(N)]
    # print(maze)
    di = [-1, 1, 0, 0]  # 상, 하, 좌, 우
    dj = [0, 0, -1, 1]
    q = []
    visited = [[0]*N for _ in range(N)]
    x, y = 0, 0
    result = 0

    # 시작점 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                x, y = i, j
    q.append((x, y))    # 시작점 인큐

    result = []  # 가능한 모든 경로의 길이를 담을 리스트
    while q:
        i, j = q.pop(0)     # 큐의 첫번째 원소를 꺼냄
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if maze[ni][nj] == '0' and visited[ni][nj] == 0:
                    q.append((ni, nj))      # 길이 있고(0), 방문한 적이 없다면 인큐
                    visited[ni][nj] = 1 + visited[i][j]    # 방문 표시(이전 인덱스의 visited에 1을 더해줌)
                    # visited[ni][nj] = 1
                if maze[ni][nj] == '3':     # 3을 만나면 도착
                    result.append(visited[i][j])    # 이전 인덱스의 visited 값
                    # result.append(d) # 강사님처럼 뎁스 사용
                    break
    if result:
        ans = min(result)
    else:
        ans = 0

    print(f'#{t+1} {ans}')