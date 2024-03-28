import sys; sys.stdin = open("input.txt")

def count(i, j, k):
    cnt = 0
    for r in range((i-k+1), (i+k)):
        if r < 0 or r >= N:
            continue
        for c in range((j-k+1), j+k):
            if c < 0 or c >= N:
                continue
            # 마름모 범위 안에 들어간다면
            if (abs(r-i) + abs(c-j)) < k:
                if arr[r][c]:
                    cnt += 1
    return cnt


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = 0
    K = 1
    while K != N+2:
        temp = 0
        cost = K ** 2 + (K - 1) ** 2
        for i in range(N):
            for j in range(N):
                cnt = count(i, j, K)
                income = cnt * M - cost
                if income > 0:
                    temp = max(temp, cnt)
        max_cnt = max(max_cnt, temp)
        K += 1

    print(f'#{t+1} {max_cnt}')