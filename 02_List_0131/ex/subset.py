N = 5
arr = [1, 2, 3, 4, 5]

for i in range(1 << N):  # 2^n을 의미 # 공집합을 빼고 싶으면 레인지를 1부터
    s = 0
    for j in range(N):
        if i & (1 << j):  # 여기서 연산이 0 or 0이 아닌 값으로 나오는데 0이 아닐때 True
            print(arr[j], end=' ')
            s += arr[j]
    print(s)    # 합도 같이 출력
