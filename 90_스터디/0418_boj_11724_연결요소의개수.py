import sys; sys.stdin = open('input.txt')

input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
# 인접 리스트
adj = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    # 무방향 그래프이므로 양쪽에서 연결해줘야 함
    adj[u].append(v)
    adj[v].append(u)

# visited 배열 생성
visited = [0]*(N+1)
cnt = 0

# x에서 시작하는 bfs
def bfs(x):
    global cnt
    queue = deque()
    queue.append(x)
    while queue:
        now = queue.popleft()
        # now에 인접한 노드들 중에서 아직 방문하지 않았다면
        for node in adj[now]:
            if visited[node] == 0:
                queue.append(node)
                visited[node] = 1

    # bfs 탐색이 끝나면 연결요소의 개수를 올린다
    cnt += 1


for x in range(1, N+1):
    # 아직 방문하지 않은 노드에서만 bfs 실행
    if visited[x] == 0:
        bfs(x)

print(cnt)