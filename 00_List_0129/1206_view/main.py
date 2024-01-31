T = 10
for t in range(T):
    N = int(input())  # 파이썬에선 필요없지만 줄바꿈을 위해..
    a = list(map(int, input().split()))
    # print(t, a)
    # a -> 앞 뒤로 2칸씩 i, i-1, i-2, i+1. i+2 가장 높은 빌딩기준으로
    # 현재의 i에 위치한 빌딩의 높이랑 얼마나 차이나는가?
    result = 0
    for i in range(2, N-2):
        # max_height = max(a[i-2:i] + a[i+1:i+3])
        max_height = max(a[i-2], a[i-1], a[i+1], a[i+2])
        current = a[i]
        result += max(0, current - max_height)  # 음수면 0으로 만들어주겠다
        # print(max_height, current, result)
    print(f'#{t+1} {result}')