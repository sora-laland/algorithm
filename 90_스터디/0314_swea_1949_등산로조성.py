import sys; sys.stdin = open("input.txt")

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 일단 k는 고려하지 않고 최장 등산로를 찾는 로직을 생각해보자
# 봉우리의 좌표는 ti, tj 로 주어진다

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
st = []
visited = [[0]*N for _ in range(N)]
max_cnt = 0

def find_route(ti, tj):
    global max_cnt

    st.append((ti, tj, 1))
    # cnt = 1
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

a = find_route(0, 1)
print(a)
