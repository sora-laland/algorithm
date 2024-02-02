T = 10
for tc in range(T):
    N = int(input())
    # arr = [0] * 100
    # for i in range(100):
    #     arr[i] = list(map(int, input().split()))
    # n = 100
    arr = [list(map(int, input().split())) for _ in range(100)]
    sum_row = [0] * 100
    sum_col = [0] * 100
    sum_cross = [0] * 2
    for i in range(100):
        sum_row[i] = sum(arr[i])
        for j in range(100):
            sum_col[j] += arr[i][j]
            if i == j:
                sum_cross[0] += arr[i][j]
            if i + j == 99:
                sum_cross[1] += arr[i][j]
    print(f'#{tc+1} {max(max(sum_row), max(sum_col), max(sum_cross))}')
    # print(sum_row)
    # print(sum_col)
    # print(sum_cross)
