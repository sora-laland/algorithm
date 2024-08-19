import sys; sys.stdin = open('input.txt')
input = sys.stdin.readline

N, C = map(int, input().split())
# 이분 탐색은 정렬된 배열에서 가능
arr = [int(input()) for _ in range(N)]
arr.sort()

# 가장 인접한 거리의 최대값을 구하여라 => 거리가 X일 때 가장 인접한 거리(& C개의 공유기)를 만족하는가?
# 최대 거리 X(초기값은 max의 절반)를 정해 놓고 C개의 공유기를 만족하는지 체크하면서 거리를 줄이거나 늘림
# mid gap의 거리를 이분탐색으로 찾아 나가기


def cnt_check(mid_gap):
    cnt = 1
    temp = arr[0]
    print('gap', mid_gap)
    for house in arr:
        if temp + mid_gap <= house:
            cnt += 1
            print(house)
            temp = house
    if cnt >= C:
        return True
    return False


min_gap = 1
# 최대 gap은 arr의 최대최소차
max_gap = arr[-1] - arr[0]
ans = 0


while min_gap <= max_gap:
    mid_gap = (min_gap + max_gap) // 2
    if cnt_check(mid_gap):
        ans = mid_gap
        # 간격이 더 커져야 함
        min_gap = mid_gap + 1
    else:
        # 간격이 더 작아져야 함
        max_gap = mid_gap - 1

print(ans)

