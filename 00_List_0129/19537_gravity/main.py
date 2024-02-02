T = int(input())
for t in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    # print(arr)
    max_fall = 0    # 최대를 0으로 설정
    for i in range(N):
        fall = 0
        for j in range(i+1, N): # i번째 보다 오른쪽에 있는 값들만 고려
            if arr[i] > arr[j]:  # i번째 값이 오른쪽 보다 크다면 떨어짐
                fall += 1
        if fall > max_fall:
            max_fall = fall
    print(f'#{t+1} {max_fall}')