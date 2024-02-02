T = int(input())
for t in range(T):
    N = int(input())
    empty_matrix = [[0] * 10 for _ in range(10)]
    count = 0
    for n in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                empty_matrix[i][j] += color
                if empty_matrix[i][j] == 3:
                    count += 1

    # print(empty_matrix)
    # print(count)
    print(f'#{t+1} {count}')
