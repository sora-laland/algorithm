from collections import deque

T = int(input())
for t in range(T):
    V, E = map(int, input().split())
    adj = [[0] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        x, y = map(int, input().split())
        adj[x][y] = 1
        adj[y][x] = 1   # 양방향
    S, G = map(int, input().split())
    visited = [0]*(V+1)
    q = deque()
    q.append((S, 0))
    answer = 0
    while q:
        node, distance = q.popleft()
        if node == G:
            answer = distance
            q.clear()
            break
        if visited[node]:
            continue
        visited[node] = 1
        for i in range(1, V+1):
            if not adj[node][i]:
                continue
            q.append((i, distance+1))
    print(f'#{t+1} {answer}')