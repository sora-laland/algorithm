N = int(input())
arr = [[0]*7 for _ in range(2)]
x = N
for i in range(4):
    arr[0][i] = x
    x += 1
y = N
for i in range(4):
    arr[1][6-i] = y
    y -= 1
print(arr)