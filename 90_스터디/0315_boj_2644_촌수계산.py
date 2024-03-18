import sys; sys.stdin = open("input.txt")

N = int(input())
tarx, tary = map(int, input().split())
M = int(input())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)
print(adj)