def binary(arr, N, key):
    start = 0
    end = N - 1
    while start <= end:
        middle = (start+end)//2
        if arr[middle] == key:
            return middle
        # 중앙값이 키보다 크면
        elif arr[middle] > key:
            end = middle - 1
        # 중앙값이 키보다 작으면
        else:
            start = middle + 1
    return -1  # 검색 실패