import sys; sys.stdin = open("input.txt")

T = int(input())
for t in range(T):

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    path = [-1] * N
    # i번 사람이 할 j번 일을 기록
    max_p = 0

    def dfs(level, cum_p):
        global max_p

        if cum_p <= max_p:
            return

        if level == N:
            if cum_p > max_p:
                max_p = cum_p
            return

        for j in range(N):
            if j in path:
                continue

            path[level] = j
            dfs(level+1, cum_p*(arr[level][j]/100))
            path[level] = -1  # 초기화 !!


    dfs(0, 1)
    print(f'#{t+1}', end=' ')
    print('{:.6f}'.format(max_p * 100))