T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, list(input())))
    print(arr)
    max_v = 0
    cnt = 0
    for i in range(N):
        if arr[i] == 1:
            cnt += 1
        else:
            continue
    if cnt < max_v:
        max_v = cnt
    print(max_v)
