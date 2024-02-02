T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    di = [0, 0, 1, 0, -1]
    dj = [0, 1, 0, -1, 0]
    sum_list = []
    for i in range(N):
        for j in range(M):
            sum_val = 0
            for k in range(5):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < M:
                    sum_val += arr[ni][nj]
            sum_list.append(sum_val)
    print(max(sum_list))
