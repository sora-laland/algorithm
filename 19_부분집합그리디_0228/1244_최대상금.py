arr = list('12834')
n = 6

max_arr = sorted(arr, reverse=True)  # 횟수에 상관없는 최대 상금
# print(max_arr)

print(arr)
for i in range(n):
    change_idx = -1

    if i < len(arr):
        idx = i
        max_idx = arr.index(max_arr[i])
        change_idx = max_idx
        if max_idx == i:
            change_idx = i-1
    if i > len(arr):
        idx = 1
        change_idx = len(arr) - 2

    arr[idx], arr[change_idx] = arr[change_idx], arr[idx]
    print(i, idx, change_idx, arr)