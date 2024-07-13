import sys; sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(R):
    global cnt
    visited[R] = cnt
    cnt += 1
    for x in adj[R]:
        if visited[x] == 0:
            dfs(x)


N, M, R = map(int, input().split())
visited = [0]*(N+1)
cnt = 1

adj = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)


for edges in adj:
    edges.sort()

dfs(R)

print(*visited[1:], sep='\n')