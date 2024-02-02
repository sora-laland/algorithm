T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0]*(N+1)]
    N += 1
    # print(arr)
    # 0을 붙이는 방법: 위와 같이
    ans = 0
    # 행 방향 탐색
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 0:
                if cnt == K:
                    ans += 1
                cnt = 0
            else:
                cnt += 1
    # print(f'#{tc+1} {ans}')
    # 이제 열방향 탐색
    for j in range(N):
        cnt = 0
        for i in range(N):
            if arr[i][j] == 0:
                if cnt == K:
                    ans += 1
                cnt = 0
            else:
                cnt += 1
    print(f'#{tc + 1} {ans}')




