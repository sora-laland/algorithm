T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    fly = []
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            sum_val = 0
            for x in range(i, i+M):
                for y in range(j, j+M):
                    sum_val += arr[x][y]
                    fly.append(sum_val)
    print(f'#{tc+1} {max(fly)}')
