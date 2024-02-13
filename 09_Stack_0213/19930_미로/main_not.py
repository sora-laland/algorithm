T = int(input())
for t in range(T):
    N = int(input())
    arr = [[1] + list(map(int, input())) + [1] for _ in range(N)]
    arr_1 = [[1]*(N+2)]
    arr_1.extend(arr)
    arr_1.append([1]*(N+2))
    st = []
    # print(arr_1)

    result = 0
    di = [-1, 1, 0, 0]  # 상하좌우
    dj = [0, 0, -1, 1]

    # print(arr)
    # 2, 3의 위치는 랜덤
    for i in range(N+2):
        for j in range(N+2):
            if arr_1[i][j] == 2:
                # print(i, j)
                st.append((i, j))  # 초기값 설정

    visited = [[0] * (N+2) for _ in range(N+2)]
    while st:
        i, j = st.pop()
        visited[i][j] = 1
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if visited[ni][nj] == 0:
                if arr_1[ni][nj] == 0:
                    st.append((ni, nj))
                if arr_1[ni][nj] == 3:
                    result = 1
                    st.clear()
                    break

    print(f'#{t+1} {result}')
