import sys; sys.stdin = open("input.txt")
arr = [int(input()) for _ in range(9)]
arr.sort()
sum_val = sum(arr)
for i in range(9):
    for j in range(i+1, 9):
        if sum_val - (arr[i] + arr[j]) == 100:
            x, y = i, j
            break
arr.pop(y)
arr.pop(x)
for _ in arr:
    print(_)

