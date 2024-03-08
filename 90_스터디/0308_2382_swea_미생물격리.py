import sys; sys.stdin = open("input.txt")

T = int(input())
for t in range(T):
    N, M, K = map(int, input().split())
    arr = []
    for _ in range(K):
        row, col, n, d = map(int, input().split())
        arr.append([row, col, n, d])
    # print(arr)

    di = [0, -1, 1, 0, 0]
    dj = [0, 0, 0, -1, 1]

    for _ in range(M):
        move_arr = []
        for a in range(len(arr)):
            n = arr[a][2]
            d = arr[a][3]
            ni = arr[a][0] + di[arr[a][3]]
            nj = arr[a][1] + dj[arr[a][3]]
            if 0<ni<N-1 and 0<nj<N-1:
                move_arr.append([ni, nj, n, d])
            else:  # 빨간 셀로 갔을 때
                n //= 2
                if d % 2:  # 홀수
                    d += 1
                else:  # 짝수
                    d -= 1
                move_arr.append([ni, nj, n, d])
        move_arr.sort(reverse=True)
        # print(move_arr)

        # 겹치는 좌표 처리
        idx = len(move_arr)-1   # 뒤에서부터 탐색한다(그래야 종료조건을 정하기 쉬움)
        while idx > 0:  # 인덱스 1까지만 탐색(이전 인덱스와 비교할 수 있어야함)
            if move_arr[idx][0] == move_arr[idx-1][0]:
                if move_arr[idx][1] == move_arr[idx-1][1]:
                    move_arr[idx-1][2] += move_arr[idx][2]
                    # 뒤 군집의 값을 앞(더 큰 미생물 개수)에 더해주고 방향 d는 앞을 따름
                    move_arr.pop(idx)
                    # 현재 뒤의 군집은 pop

            idx -= 1    # 다음으로 한 칸 앞의 인덱스를 검사해야 함

        arr = move_arr  # 배열을 갱신

    # print(arr)  # 최종 배열
    sum_val = 0
    for item in arr:
        sum_val += item[2]

    print(f'#{t+1} {sum_val}')