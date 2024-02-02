T = 10
for _ in range(T):
    tc = int(input())
    board = [list(map(int, input().split()))
             for _ in range(100)]
    # point = board[99].index(2)
    # r, c = 99, point

    result = 0
    for i in range(100):
        col = i
        if board[0][col] == 0:  # 각 열의 첫 행이 0이면 필요 없음
            continue
        row = 0
        direction = 0  # 현재 어느방향을 탐색
        while r < 99:
            # 방향
            if direction == 0:  # 아래로 내려가고있는 경우
                if (col-1) >= 0 and board[row][(col-1)] == 1:
                    direction = 1   # 방향을 왼쪽으로 꺾어줌
                if (col+1) < 100 and board[row][(col+1)] == 1:
                    direction = 2   # 오른쪽으로 꺾어줌

            if direction != 0:  # 아래로 내려가고있지 않은 경우
                if board[row+1][col] == 1:  # 아래에 길이 있는 경우
                    direction = 0
            # 이동
            if direction == 0:
                row += 1  # 아래로 이동
            elif direction == 1:
                col -= 1    # 왼쪽으로 이동
            elif direction == 2:
                col += 1    # 오른쪽으로 이동
            print(row, col)
        if board[row][col] == 2:
            print('출발', i, '도착', col)
            result = i
            break
        print(f'#{tc} {result}')
