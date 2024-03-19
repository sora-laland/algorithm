import sys; sys.stdin = open("input.txt")
from collections import deque

N = int(input())
tarx, tary = map(int, input().split())
M = int(input())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)
# print(adj)
visited = [0] * (N+1)
q = deque()

def bfs(start, end):
    cnt = 0
    q.append(start)
    while q:
        w = q.popleft()
        visited[w] = 1  # 방문 표시
        cnt += 1
        for node in adj[w]:
            if visited[node]:
                continue
            q.append(node)
            if node == end:
                return cnt
    return -1


print(bfs(tarx, tary))