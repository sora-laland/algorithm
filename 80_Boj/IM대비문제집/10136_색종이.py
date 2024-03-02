import sys; sys.stdin = open("input.txt")

N = int(input())
plate = [[0]*1001 for _ in range(1001)]
for n in range(1, N+1):
    x, y, w, h = map(int, input().split())
    # 색칠
    for i in range(x, x+w):
        for j in range(y, y+h):
            plate[i][j] = n

# 마지막에 세주기
cnt_list = [0] * 100
for lst in plate:
    for i in lst:
        if i:
            cnt_list[i-1] += 1
for i in range(N):
    print(cnt_list[i])