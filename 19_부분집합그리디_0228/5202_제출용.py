import sys; sys.stdin = open("5202.txt")

T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort(key=lambda x: x[1])
    # print(arr)
    # 초기값(종료시간) 설정
    end = arr[0][1]
    cnt = 1  # 첫번째 화물
    for cargo in arr:
        if cargo[0] >= end:
            end = cargo[1]
            cnt += 1
    print(f'#{t+1} {cnt}')