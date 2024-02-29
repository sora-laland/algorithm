import sys; sys.stdin = open("4615.txt")
T = int(input())
di = [-1, -1, -1, 0, 0, 1, 1, 1]  # 8방향
dj = [-1, 0, 1, -1, 1, -1, 0, 1]


def get_reverse_stone(i, j, bang, color):
    ni, nj = i, j
    result = []
    while True:
        ni = ni + di[bang]  # 해당 방향으로 한 칸 더 이동
        nj = nj + dj[bang]
        if not (0<=ni<N and 0<=nj<N):    # 범위를 벗어나면
            return []
        if plate[ni][nj] == 0:  # 더이상 돌이 없으면
            return []
        if plate[ni][nj] == color:  # 나와 같은 돌을 만나면
            break
        result.append((ni, nj))  # 그 전까지 반대색 돌 좌표를 기록
    return result


for t in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]

    plate = [[0] * N for _ in range(N)]  # 초기 돌 착수
    plate[(N//2)-1][(N//2)-1] = 2
    plate[(N//2)][(N//2)-1] = 1
    plate[(N//2)-1][(N//2)] = 1
    plate[(N//2)][(N//2)] = 2

    # plate[1][0] = 1
    # a = get_reverse_stone(1, 0, 4, 1)
    # print(a)

    print(plate)
    for stone in arr:
        x, y, color = stone
        plate[y-1][x-1] = color
        for bang in range(8):
            changes = get_reverse_stone(y-1, x-1, bang, color)
            for change in changes:
                i, j = change
                if plate[i][j] == 1:
                    plate[i][j] = 2
                else:
                    plate[i][j] = 1
    # print(plate)
    # 2차원 배열에서 1과 2의 개수를 세야한다
    cnt1 = 0
    cnt2 = 0
    for lst in plate:
        cnt1 += lst.count(1)
        cnt2 += lst.count(2)
    print(f'#{t+1} {cnt1} {cnt2}')

