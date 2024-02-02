di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

N = 5
i = 3
j = 4
arr = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            print((ni, nj), end=' ')
        print()
# 강의 보고 출력부분 추가하기