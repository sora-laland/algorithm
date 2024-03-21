graph_l = [
    [1, 3],
    [0, 2, 4],
    [1],
    [0, 4],
    [1, 3]
]
visited = [0] * 5
path =[]


def dfs(now):
    for to in graph_l[now]:
        # 이미 방문했다면 pass
        if visited[to] == 1:
            continue

        visited[to] = 1
        path.append(to)
        dfs(to)


visited[0] = 1
path.append(0)

dfs(0)
print(path)