graph_m = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 0, 0],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0],
]
visited = [0] * 5

# 여기선 큐를 리스트로 구현하지만
# 문제 풀 땐 deque을 활용할 것

def bfs(start):
    # 시작점 인큐
    queue = [start]
    visited[start] = 1

    while queue:
        now = queue.pop(0)
        print(now, end=' ')

        # 인접행렬이므로 접점을 반복문으로 탐색
        for to in range(5):
            if graph_m[now][to] == 0:
                continue
            if visited[to]:
                continue

            visited[to] = 1
            # print(visited)
            queue.append(to)

bfs(0)