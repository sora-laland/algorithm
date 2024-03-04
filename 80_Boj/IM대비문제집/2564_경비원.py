import sys; sys.stdin = open("input.txt")

W, H = map(int, input().split())
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dg_direc, dg_dist = map(int, input().split())

# 1북 2남 3서 4동
sum_distance = 0
for spot in arr:
    direc = spot[0]
    dist = spot[1]
    peri = 2*(W+H)
    temp = 0

    if direc == dg_direc:  # 상점과 동근이가 같은 방향에 있을 때
        sum_distance += abs(dist - dg_dist)

    elif dg_direc == 1:    # 동근이가 북쪽에 있을 때
        if direc == 2:
            temp = dg_dist + H + dist
        elif direc == 3:
            temp = dg_dist + dist
        elif direc == 4:
            temp = (W - dg_dist) + dist
        sum_distance += min(temp, peri - temp)

    elif dg_direc == 2:    # 동근이가 남쪽에 있을 때
        if direc == 1:
            temp = dg_dist + H + dist
        elif direc == 3:
            temp = dg_dist + (H - dist)
        elif direc == 4:
            temp = (W - dg_dist) + (H - dist)
        sum_distance += min(temp, peri - temp)

    elif dg_direc == 3:    # 동근이가 서쪽에 있을 때
        if direc == 1:
            temp = dg_dist + dist
        elif direc == 2:
            temp = (H - dg_dist) + dist
        elif direc == 4:
            temp = dg_dist + W + dist
        sum_distance += min(temp, peri - temp)

    elif dg_direc == 4:    # 동근이가 동쪽에 있을 때
        if direc == 1:
            temp = dg_dist + (W - dist)
        elif direc == 2:
            temp = (H - dg_dist) + (W - dist)
        elif direc == 3:
            temp = dg_dist + W + dist
        sum_distance += min(temp, peri - temp)

print(sum_distance)
# 한 방향의 거리는 (트랙 - 다른 방향의 거리)