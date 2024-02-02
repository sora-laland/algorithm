import sys

sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    sum_list = []
    for i in range(N):
        for j in range(M):
            sum_val = 0
            sum_val += arr[i][j]
            for k in range(4):
                for n in range(1, arr[i][j]+1):
                    ni = i + n * di[k]
                    nj = j + n * dj[k]
                    if 0 <= ni < N and 0 <= nj < M:
                        sum_val += arr[ni][nj]
            sum_list.append(sum_val)
    print(sum_list)
    print(f'#{t+1} {max(sum_list)}')