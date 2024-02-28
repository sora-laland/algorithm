import sys; sys.stdin = open("10760.txt")

di = [-1, -1, -1, 0, 0, 1, 1, 1]  # 8방향
dj = [-1, 0, 1, -1, 1, -1, 0, 1]

T = int(input())
for t in range(T):
    N, M = map(int, input().split())    # N*M 행렬
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 8방향을 탐색하면서 타겟보다 값이 작으면 카운트
    # 카운트가 4 이상이면 후보지 카운트
    print(f'#{t+1}', end=' ')
    cnt = 0
    for i in range(N):
        for j in range(M):
            target = arr[i][j]
            photo_cnt = 0
            for k in range(8):
                ni = i + di[k]
                nj = j + dj[k]
                if not (0<=ni<N and 0<=nj<M):
                    continue
                if arr[ni][nj] < target:
                    photo_cnt += 1
            if photo_cnt >= 4:
                cnt += 1
    print(cnt)