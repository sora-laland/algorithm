import sys; sys.stdin = open("input.txt")
plate = [[0] * 100 for _ in range(100)]
N = int(input())
for n in range(N):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            plate[i][j] = 1

sum_val = 0
for r in plate:
    sum_val += sum(r)
print(sum_val)