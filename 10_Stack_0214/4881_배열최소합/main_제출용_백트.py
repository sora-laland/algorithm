def f(i, k, sum_v):
    global min_sum
    if i == k:
        if min_sum > sum_v:
            min_sum = sum_v
    elif min_sum <= sum_v:
        return
    else:
        for j in range(i, k):   # P[i]자리에 올 원소 P[j]
            P[i], P[j] = P[j], P[i]     # P[i] <-> P[j]
            f(i+1, k, sum_v + arr[i][P[i]])  # 값을 더해줌
            P[i], P[j] = P[j], P[i]     # 교환전으로 복구


T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    P = [i for i in range(N)]
    min_sum = 100
    f(0, N, 0)
    print(f'#{t+1} {min_sum}')
