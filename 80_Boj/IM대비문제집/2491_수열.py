import sys; sys.stdin = open("input.txt")

N = int(input())
arr = list(map(int, input().split()))
common_diff = [arr[i]-arr[i-1] for i in range(1, N)]

# 추후에 고침
up_cnt = 1
down_cnt = 1
max_up_cnt = 1
max_down_cnt = 1
for j in range(1, N-1):
    if common_diff[j-1] >= 0:
        if common_diff[j] >= 0:
            up_cnt += 1
        else:
            up_cnt = 1
    if up_cnt > max_up_cnt:
        max_up_cnt = up_cnt
    if common_diff[j-1] <= 0:
        if common_diff[j] <= 0:
            down_cnt += 1
        else:
            down_cnt = 1
    if down_cnt > max_down_cnt:
        max_down_cnt = down_cnt

if N == 1:
    print(max(max_up_cnt, max_down_cnt))
else:
    print(max(max_up_cnt, max_down_cnt) + 1)

# 처음에 틀린 답
# cnt = 0
# max_cnt = 0
# for j in range(N-2):
#     if common_diff[j] >= 0:
#         if common_diff[j+1] >= 0:
#             cnt += 1
#         else:
#             cnt = 0
#     elif common_diff[j] <= 0:
#         if common_diff[j+1] <= 0:
#             cnt += 1
#         else:
#             cnt = 0
#     if cnt > max_cnt:
#         max_cnt = cnt
# # print(common_diff)
# if N == 1:
#     print(max_cnt + 1)
# else:
#     print(max_cnt + 2)
