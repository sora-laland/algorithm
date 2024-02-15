T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for lst in arr:
        for i in range(2):
            if lst[i] % 2 == 0:  # 짝수라면 1을 빼서 홀수로 만들어줌
                lst[i] -= 1
    blank = [0] * 401
    for lst in arr:
        if lst[0] < lst[1]:
            for i in range(lst[0], lst[1]+1):
                blank[i] += 1
        else:   # 출발 방 번호가 더 큰 경우
            for i in range(lst[1], lst[0]+1):
                blank[i] += 1
    print(f'#{t+1} {max(blank)}')
