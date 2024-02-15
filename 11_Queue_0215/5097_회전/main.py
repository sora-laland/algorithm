N, M = map(int, input().split())
cQ = [0] + list(map(int, input().split()))

print(cQ)
# 이미 차있는 상태
front = 1
rear = N
# deQ
a = cQ[front]
# enQ
cQ[rear] = a
print(cQ)
