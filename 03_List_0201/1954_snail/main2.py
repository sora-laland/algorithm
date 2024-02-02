T = int(input())
for t in range(T):
    N = int(input())
    board = [[0] * N for _ in range(N)]
    r, c = 0, 0   # 빈 행렬의 인덱스
    direction = 0
    for i in range(1, N**2+1):  # 1부터 n제곱 까지 반복
        board[r][c] = i
        if direction == 0 and (c == N-1 or board[r][c+1]):
            # 오른쪽으로 가다가 끝을 만나거나(c == N-1) 다음 인덱스(c+1)에 값이 있을것으로 예상되면(인덱스[r][c+1]가 0이 아니면) 방향 바꾸기
            direction = 1
        elif direction == 1 and (r == N-1 or board[r+1][c]):  # 아래로 가다가 끝 만나면 왼쪽으로 방향 전환
            direction = 2
        elif direction == 2 and (c == 0 or board[r][c-1]):
            direction = 3
        elif direction == 3 and (r == 0 or board[r-1][c]):
            direction = 0
        # 이제 방향에 맞게 보드의 인덱스를 움직인다
        if direction == 0:
            c += 1
        elif direction == 1:
            r += 1
        elif direction == 2:
            c -= 1
        elif direction == 3:
            r -= 1

    # 출력
    print(f'#{t+1}')
    for row in board:  # 행렬 출력
        print(*row)   # 언패킹
