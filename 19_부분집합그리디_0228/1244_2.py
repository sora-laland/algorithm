arr = list('456789')
n = 10

max_arr = sorted(arr, reverse=True)  # 횟수에 상관없는 최대 상금
print(max_arr)

lst = []
print(arr)
for i in range(n):
    if i < len(arr):
        idx = i
        # 인덱스 대신에 뒤에서부터 찾기
        for x in range(len(arr)-1, -1, -1):
            if arr[x] == max_arr[i]:
                max_idx = x
                break

        change_idx = max_idx
        if max_idx == i:
            change_idx = i-1
        arr[idx], arr[change_idx] = arr[change_idx], arr[idx]
    else:
        idx = -1
        change_idx = -2
        arr[idx], arr[change_idx] = arr[change_idx], arr[idx]
    print(idx, change_idx, arr)

