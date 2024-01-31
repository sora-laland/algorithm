T = 10


def counting(arr):
    k = max(arr)
    counts = [0] * (k+1)
    length = len(arr)
    for i in range(length):
        counts[arr[i]] += 1
    return counts


for tc in range(T):
    dump = int(input())
    heights = list(map(int, input().split()))
    counted = counting(heights)
    start = 1    # 현재 가장 작은 건물의 높이
    end = len(counted)-1      # 현재 가장 큰 높이
    while dump > 0:
        # if counted[start] == 0:     # 스타트가 0이 아니어야 하니까 만약 0이라면 다음으로 넘어가서 스타트로해
        if not counted[start]:
            start += 1
            continue
        if not counted[end]:
            end -= 1
            continue
        counted[start] -= 1
        counted[start+1] += 1
        counted[end] -= 1
        counted[end] += 1
        dump -= 1      # 평탄화작업 진행중
        # 한번 더 중앙으로 움직이는 것 검사
        if not counted[start]:
            start += 1
        if not counted[end]:
            end -= 1
    print(f'{tc+1} {end - start}')
