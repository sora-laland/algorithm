import sys; sys.stdin = open("input.txt")

def dfs(now):
    for to in adj[now]:
        # 이미 방문했다면 pass
        if visited[to] == 1:
            continue

        visited[to] = 1
        path.append(to)
        dfs(to)


T = int(input())
for t in range(T):
    print(f'#{t+1}', end=' ')
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    adj = [[] for _ in range(N+1)]
    for i in range(0, (2 * M), 2):
        s = arr[i]
        e = arr[i + 1]
        adj[s].append(e)
        adj[e].append(s)
    # print(adj)
    teams = []
    for i in range(1, N+1):
        visited = [0] * (N+1)
        path = []

        visited[i] = 1
        path.append(i)

        dfs(i)
        team = min(path)
        if team not in teams:
            teams.append(team)
    print(len(teams))
