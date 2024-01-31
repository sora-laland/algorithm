T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    # print(N, M)
    a = list(map(int, input().split()))
    min_val = 1000000000    # 충분히 큰 값을 줘야함
    max_val = 0
    for n in range(N - M + 1):
        sum_val = sum(a[n:n+M])
        max_val = max(max_val, sum_val)
        min_val = min(min_val, sum_val)
        # print('min', min_val, 'max', max_val, 'sum', sum_val)

    print(f'#{t} {max_val - min_val}')