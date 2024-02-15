def rcp(idx1, idx2):
    # 여기서 항상 idx1 < 2이고, 비긴 경우엔 idx1 승 (idx2를 기준으로 하는 게 쉽다)
    if (arr[idx1] - arr[idx2]) == -1 or (arr[idx1] - arr[idx2]) == 2:  # idx2가 이긴 경우
        return idx2 # 승자를 리턴
    return idx1


T = int(input())
for t in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    start = 1
    end = N
    mid = (start+end)//2
    while start == end:
        g1 = (start, mid+1)
        g2 = (mid, end+1)

    # print(rcp(0, 2))