graph_l = [
    [1, 3],
    [0, 2, 4],
    [1],
    [0, 4],
    [1, 3]
]
visited = [0] * 5

def bfs(start):
    # 시작점 인큐
    queue = [start]
    visited[start] = 1

    while queue:
        now = queue.pop(0)
        print(now, end=' ')

        # 인접행렬이므로 접점을 반복문으로 탐색
        for to in graph_l[now]:
            if visited[to]:
                continue

            visited[to] = 1
            # print(visited)
            queue.append(to)

bfs(0)