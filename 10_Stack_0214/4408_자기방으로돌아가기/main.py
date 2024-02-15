T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for lst in arr:
        for i in range(2):
            if lst[i] % 2:  # 홀수
                lst[i] = (lst[i]+1) // 2
            else:
                lst[i] //= 2
    blank = [0] * 201
    for lst in arr:
        if lst[0] < lst[1]:
            for i in range(lst[0], lst[1]+1): # 여기에 +1?
                blank[i] += 1
        else:   # 출발 방번호가 더 큰 경우
            for i in range(lst[1], lst[0]+1):
                blank[i] += 1
    print(blank)
    print(arr)
    print(f'#{t+1} {max(blank)}')
