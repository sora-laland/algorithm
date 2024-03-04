import sys; sys.stdin = open("input.txt")

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
Time = t % ((w*h)-1)    # 반복되는 시간 줄이기

i, j = p, q
di = dj = 1  # 초기값
# 좌,상:0   우,하:1
for a in range(Time):
    # print(i, j)

    # 상향일 때 윗벽을 만나면 하향으로 바꿔줌
    # 하향일 때 아랫벽을 만나면 상향으로 바꿔줌
    if di == -1 and i == 0:
        di = 1
    elif di == 1 and i == w:
        di = -1

    # 좌향일 때 왼쪽벽을 만나면 우향으로
    # 우향일 때 오른쪽 벽을 만나면 좌향으로
    if dj == -1 and j == 0:
        dj = 1
    elif dj == 1 and j == h:
        dj = -1

    i += di
    j += dj

print(i, j)
