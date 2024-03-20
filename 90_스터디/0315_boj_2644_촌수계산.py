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

def bfs(start):
    q.append(start)
    visited[start] = 1
    while q:
        w = q.popleft()
        for node in adj[w]:
            if visited[node]:
                continue
            q.append(node)
            visited[node] = visited[w] + 1


bfs(tarx)
if visited[tary]:
    print(visited[tary]-1)
else:
    print(-1)