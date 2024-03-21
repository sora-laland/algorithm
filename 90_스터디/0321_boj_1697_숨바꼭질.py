import sys; sys.stdin = open("input.txt")
from collections import deque

N, K = map(int, input().split())
q = deque()
visited = [0] * 100001
# 시작점 인큐
q.append(N)

while q:
    now = q.popleft()

    if now == K:
        break

    minus = now-1
    plus = now+1
    double = now*2

    for next in [minus, plus, double]:
        if 0 <= next <= 100000:
            if visited[next]:
                continue
            q.append(next)
            visited[next] = visited[now] + 1

print(visited[K])