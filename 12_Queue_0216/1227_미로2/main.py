T = 10
for t in range(T):
    tc = int(input())
    maze = [input() for _ in range(100)]
    # print(maze)
    di = [-1, 1, 0, 0]  # 상, 하, 좌, 우
    dj = [0, 0, -1, 1]
    q = []
    visited = [[0]*100 for _ in range(100)]
    q.append([1, 1])    # 시작점 인큐
    result = 0

    while q:
        a = q.pop(0)     # 큐의 첫번째 원소를 꺼냄
        for k in range(4):
            ni = a[0] + di[k]
            nj = a[1] + dj[k]
            if maze[ni][nj] == '0' and visited[ni][nj] == 0:
                q.append([ni, nj])      # 길이 있고(0), 방문한 적이 없다면 인큐
                visited[ni][nj] = 1     # 방문 표시
            if maze[ni][nj] == '3':     # 3을 만나면 도착
                result = 1
                break
    print(f'#{tc} {result}')