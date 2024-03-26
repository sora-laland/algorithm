import sys; sys.stdin = open("input.txt")
from collections import deque
F, S, G, U, D = map(int, input().split())
# S에서 G로 몇번만에?
# visited와 queue 활용

# 인덱스 0은 버림
visited = [0] * (F+1)

q = deque()
q.append(S)
visited[S] = 1
while q:
    now = q.popleft()
    if now == G:
        break
    if (0 < now+U <= F) and visited[now+U] == 0:
        q.append(now+U)
        visited[now+U] = visited[now] + 1
    if (0 < now-D <= F) and visited[now-D] == 0:
        q.append(now-D)
        visited[now-D] = visited[now] + 1

print(visited)
ans = visited[G]
if ans:
    print(ans-1)
else:
    print('use the stairs')
