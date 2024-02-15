from collections import deque

# 선형큐이자 linked list 큐로 동작함
# q = deque()
# q.append(1)
# q.append(2)
# q.append(3)
# print(q.popleft())
# print(q.popleft())


q = []
for i in range(10000):
    q.append(i)
print('append')
while q:
    q.pop(0)
print('end')

# 실행 속도가 훨씬 빠름
dq = deque()
for i in range(10000):
    dq.append(i)
print('append')
while dq:
    dq.popleft()
print('end')