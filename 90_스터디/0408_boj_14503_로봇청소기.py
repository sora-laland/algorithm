import sys; sys.stdin = open("input.txt")

N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def check(i, j):
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if not (0<=ni<N and 0<=nj<M):
            continue
        # 빈칸이 있는 경우
        if arr[ni][nj] == 0:
            return False
    # 청소되지 않은 빈칸이 없는 경우
    else:
        return True

# print(check(0, 1))


def move(i, j, d):
    mi = i + di[d]
    mj = j + dj[d]
    return mi, mj


i, j = r, c
cnt = 0
while True:
    if arr[i][j] == 0:
        arr[i][j] = 2
        cnt += 1
    if check(i, j):
        # 후진할 수 있다면
        back_d = (d + 2) % 4
        mi, mj = move(i, j, back_d)
        if arr[mi][mj] == 1:
            # 멈춘다
            break
        else:
            # 후진한다
            i, j = mi, mj
    # 청소되지 않은 빈칸이 있다면
    else:
        # 반시계 90도 회전
        d = (d - 1) % 4
        mi, mj = move(i, j, d)
        if arr[mi][mj] == 0:
            # 전진
            i, j = mi, mj

print(cnt)


