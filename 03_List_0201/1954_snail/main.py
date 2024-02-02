n = 3
snail = [[0] * n for _ in range(n)]  # 빈 행렬
num = list(range(1, n**2+1))
# print(num)
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


num = 1
for i in range(n):
    for j in range(n+5):
        snail[i][j] = num
        num += 1

print(snail)