T = int(input())
for t in range(T):
    N = int(input())
    maze = []
    for _ in range(N):
        maze.append(input())
    result = 0
    st = []
    di = [-1, 1, 0, 0]  # 상하좌우 ,, 짝만 맞으면 노상관
    dj = [0, 0, -1, 1]  # 델타탐색
    # print(maze)
    # 2와 3은 랜덤으로 존재
    # 우선 2를 찾아야한다(시작점)
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':  # 문자열임을 주의(숫자로 바꾸지 않은 상태)
                st.append([i, j])   # 시작 좌표를 쌍으로 넣어줌(튜플로 넣어도 됨)
    # 탐색 시작 -> 재귀, BFS..
    # 특정 좌표 방문을 기록하는 리스트
    visited = [[0] * N for _ in range(N)]
    while st:
        i, j = st.pop()  # [i, j] 형태
        visited[i][j] = 1  # 방문 여부 체크
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            # 미로 범위를 넘는지 확인
            # 혹시 방문했던 곳인지 확인
            if 0 <= ni < N and 0 <= nj < N and (visited[ni][nj] == 0):
            # if not (0 <= ni < N):   # ni 좌표검사
            #     continue      # continue/break는 가장 근처에 있는 반복문에 적용
            # if not (0 <= nj < N):   # nj 좌표검사
            #     continue
            # if visited[ni][nj]:  # 방문 여부 검사
            #     continue

            # 0, 1, 3
            # 0: 이동 가능함
                if maze[ni][nj] == '0':
                    st.append([ni, nj])     # 스택에 푸쉬
                # 1의 경우, 하지 않음을 구현할 필요 X
                if maze[ni][nj] == '3':
                    result = 1
                    st.clear()  # 스택을 비워서 더이상 가망없는 혹은 쓸데없는 탐색을 그만함, 뒤에 방문할 수도 있는 경로를 없애버림, while 종료
                    break  # 델타(방향)에 대한 브레이크, k for문 종료

    print(f'#{t+1} {result}')