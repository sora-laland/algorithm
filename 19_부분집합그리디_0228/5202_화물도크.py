import sys; sys.stdin = open("5202.txt")

T = int(input())
for t in range(T):
    print(f'#{t+1}', end=' ')
    N = int(input())

    request = [list(map(int, input().split())) for _ in range(N)]
    # request.sort(key=lambda x: x)
    # print(request)
    request.sort(key=lambda x: x[1])    # 종료 시간을 기준으로 정렬
    # print(request)
    # request.sort(key=lambda x: x[0])
    # print(request)
    # request.sort(key=lambda x: (x[0], x[1]))
    # print(request)
    # request.sort(key=lambda x: -x[0])
    # print(request)
    # request.sort(key=lambda x: (x[0], -x[1]))
    # print(request)

    # 맨 처음 회의는 어차피 받고 시작
    end_time = request[0][1]
    cnt = 1
    for s, e in request:
        if end_time <= s:
            cnt += 1
            end_time = e    # 새로운 시간으로 갱신해줌
            # 이 경우만 생각하면 됨
    print(cnt)