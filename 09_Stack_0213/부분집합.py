def f(i, k):
    if i == k:
        for j in range(k):
            if bit[j]:
                print(arr[j], end=' ')
        print()
    else:
        for j in range(2):
            bit[i] = j
            f(i+1, k)
        # 여기서 for를 쓰지 않고 j에 0과 1을 각각 넣어도 됨
        # 교재에선 변수가 캔디데이트 어쩌고라 어려워 보임


N = 4
arr = [1, 2, 3, 4]
bit = [0]*N
f(0, N)     # bit[i]에 1또는 0을 채우고, N개의 원소가 결정되면 부분집합을 출력