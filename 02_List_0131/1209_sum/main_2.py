T = 10
for tc in range(T):
    N = int(input())
    n = 100
    arr = [0] * n
    arr = [list(map(int, input().split())) for _ in range(n)]
    sum_row = [0] * n
    sum_col = [0] * n
    sum_cross = [0] * 2
    for i in range(n):
        for j in range(n):
            sum_row[i] += arr[i][j]
            sum_col[j] += arr[i][j]
            if i == j:
                sum_cross[0] += arr[i][j]
            if i + j == n-1:
                sum_cross[1] += arr[i][j]
    print(f'#{tc+1} {max(max(sum_row), max(sum_col), max(sum_cross))}')