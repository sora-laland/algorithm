import sys; sys.stdin = open("input.txt")

N, K = map(int, input().split())
arr = list(map(int, input().split()))

# max_val = (-100) * K
# for i in range(0, N-K+1):
#     sum_val = sum(arr[i:i+K])
#     if sum_val > max_val:
#         max_val = sum_val
# print(max_val)
# 이렇게 하면 시간초과 >> 투포인터 이용

sum_val = max_val = sum(arr[0:K])
for i in range(K, N):
    sum_val = sum_val - arr[i-K] + arr[i]
    max_val = max(max_val, sum_val)
print(max_val)