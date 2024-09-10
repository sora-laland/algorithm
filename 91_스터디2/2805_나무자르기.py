import sys; sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

# H의 최대값을 구하라

# 자른 길이 : 전체 나무 길이의 합
# H의 최소
left = 0
# 자른 길이 : 0
# H의 최대
right = max(arr)


while left <= right:

    mid = (left + right) // 2
    H = mid
    sum_val = 0
    for tree in arr:
        if tree > H:
            sum_val += (tree - H)


    # print(left, right, mid, sum_val)
    if mid == left:
        break


    # 필요한 길이 만족 -> H를 높여봄
    if sum_val >= M:
        left = mid
    # 필요한 길이보다 작으면 -> H 줄여서 더 자르기
    else:
        right = mid

print(H)