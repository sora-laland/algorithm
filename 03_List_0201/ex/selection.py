def selection(a, N):
    #  구간의 시작 i
    for i in range(N-1): # 구간이 시작 1, 2 개의 원소가 남을 때 까지
        min_idx = i
        # 구간에서 실제 최소값 찾기, 실제 최소값을 찾을 위치 j
        for j in range(i+1, N):
            if a[min_idx] > a[j]:
                min_idx = j
        a[min_idx], a[i] = a[i], a[min_idx]  # 맞바꾸기
    return
# 가능하면 함수 정의는 몰아서 하기

N = 5
arr = [1, 3, 2, 5, 4]
print(arr)
selection(arr, N)
print(arr)
