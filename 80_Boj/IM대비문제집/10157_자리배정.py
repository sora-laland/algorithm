import sys; sys.stdin = open("input.txt")

# swea 달팽이 참조
C, R = map(int, input().split())
K = int(input())

arr = [[0] * R for _ in range(C)]
# print(arr)
i, j = 0, 0  # 초기값
di = 1

if K > C*R:
    print(0)
else:
    for n in range(1, C*R+1):   # 일단 다 채우기
        arr[i][j] = n

        if n == K:
            print(i+1, j+1)
            break

        # 이제 특정 조건에서 방향을 바꿔준다
        if di == 1 and (j == R-1 or arr[i][j+1] != 0):
            # 오른쪽으로 가기로 되어있는데 현재 끝 값이거나 다음칸이 이미 차있다면 아래로 방향 바꾼다
            di = 2
        elif di == 2 and (i == C-1 or arr[i+1][j] != 0):
            # 아래로 가기로 되어있는데 현재 끝 값이거나 다음칸이 이미 차있다면 왼쪽으로 방향 바꾼다
            di = 3
        elif di == 3 and (j == 0 or arr[i][j-1] != 0):
            # 왼쪽으로 가기로 되어있는데 현재 끝 값이거나 다음칸이 이미 차있다면 위로 방향 바꾼다
            di = 4
        elif di == 4 and (i == 0 or arr[i-1][j] != 0):
            # 위로 가기로 되어있는데 현재 끝 값이거나 다음칸이 이미 차있다면 오른쪽으로 방향 바꾼다
            di = 1
        # 방향에 따른 이동
        if di == 1: j += 1      # 우
        elif di == 2: i += 1    # 하
        elif di == 3: j -= 1    # 좌
        elif di == 4: i -= 1    # 상
