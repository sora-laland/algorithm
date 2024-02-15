def f(i, k):
    global cnt
    global min_sum
    cnt += 1
    if i == k:
        sum_v = 0
        for j in range(k):
            sum_v += arr[j][P[j]]
        if min_sum > sum_v:
            min_sum = sum_v
    else:
        for j in range(i, k):   # P[i]자리에 올 원소 P[j]
            P[i], P[j] = P[j], P[i]     # P[i] <-> P[j]
            f(i+1, k)
            P[i], P[j] = P[j], P[i]     # 교환 전으로 복구


T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    # P[i]: arr의 i행에서 몇열(j)(열이 중복되면 안된다)을 고를건지?
    # 기본 P의 형태: [0, 1, 2, ... N-1]
    P = [i for i in range(N)]
    min_sum = 100
    cnt = 0
    f(0, N)
    print(f'#{t+1} {min_sum} {cnt}')
    # print(min_sum)
    # 제한시간 초과로 백트랙킹 적용해야함
