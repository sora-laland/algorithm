import sys; sys.stdin = open("input.txt")

# 빈 2차원 리스트에 좌표에 맞게 색칠하고 배열을 더한다
rect = [list(map(int, input().split())) for _ in range(4)]
arr = [[0]*100 for _ in range(100)]
result = 0
# print(arr)
for r in range(4):
    x1, y1, x2, y2 = rect[r]
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i][j] = 1   # 겹치는 부분도 결국 1

for k in arr:
    result += sum(k)
print(result)