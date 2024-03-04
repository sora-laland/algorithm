import sys; sys.stdin = open("input.txt")

N = int(input())
arr = [0] * 1001
for _ in range(N):
    idx, h = map(int, input().split())
    arr[idx] = h


def find_max():
    idx1 = 0
    idx2 = 1000
    max_val = max(arr)
    for i in range(1001):
        if arr[i] == max_val:
            idx1 = i
            break
    for j in range(1000, -1, -1):
        if arr[j] == max_val:
            idx2 = j
            break
    return idx1, idx2


idx1, idx2 = find_max()

# max 기둥보다 왼쪽의 면적
area1 = 0
max1 = 0
for i in range(0, idx1):
    max1 = max(max1, arr[i])
    area1 += max1
# print(area1)

# max 기둥의 면적
area_m = (idx2 - idx1 + 1) * max(arr)
# print(area_m)

# max 기둥보다 오른쪽의 면적
area2 = 0
max2 = 0
for j in range(1000, idx2, -1):
    max2 = max(max2, arr[j])
    area2 += max2
# print(area2)

print(area1 + area_m + area2)