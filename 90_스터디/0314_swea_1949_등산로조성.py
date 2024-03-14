import sys; sys.stdin = open("input.txt")


# 일단 k는 고려하지 않고 최장 등산로를 찾는 로직을 생각해보자
# 봉우리의 좌표는 ti, tj 로 주어진다

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
# max_cnt = 0


def find_route(ti, tj):
    global max_cnt
    st = []
    visited = [[0]*N for _ in range(N)]
    st.append((ti, tj, 1))
    while st:
        i, j, c = st.pop()
        visited[i][j] = 1
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni<0 or ni>=N or nj<0 or nj>=N:
                continue
            if visited[ni][nj]:
                continue
            if arr[ni][nj] < arr[i][j]:  # 이동 가능
                c += 1
                st.append((ni, nj, c))
                if c > max_cnt:
                    max_cnt = c
                c -= 1
    return max_cnt


T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 봉우리 찾기
    peaks = []
    max_height = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > max_height:
                max_height = arr[i][j]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == max_height:
                peaks.append((i, j))
    # print(peaks)

    # 각각의 봉우리에서 시작해서
    # 자신을 제외한 모든 지점을 0~k 만큼 깎아서 경로 구하기

    routes = []

    for peak in peaks:
        for i in range(N):
            for j in range(N):
                # 봉우리가 아닌 곳만 깎는다
                if i != peak[0] or j != peak[1]:
                    for k in range(K+1):
                        max_cnt = 0
                        arr[i][j] -= k
                        route = find_route(peak[0], peak[1])
                        routes.append(route)
                        arr[i][j] += k      # 다시 더해줌

    print(max(routes))