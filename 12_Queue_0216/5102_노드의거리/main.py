def bfs(s, N, G):  # 시작정점 s, 노드개수 N
    q = []                  # 큐
    visited = [0]*(N+1)     # visited,, 맨 앞의 0인덱스는 쓰지 않음
    q.append(s)             # 시작점 인큐
    visited[s] = 1          # 시작점 방문(인큐)표시
    # 큐가 비워질때까지...(남은 정점이 있으면)
    while q:
        t = q.pop(0)        # 앞에걸 꺼내
        # t에서 할 일...
        if t == G:
            return visited[t]-1     # 몇개의 간선을 지나가는지?
        # print(t)
        for i in adjl[t]:   # t에 인접인 정점 i 꺼내
            if visited[i] == 0:     # t의 인접 정점이 방문하지 않은 정점이면(처리된 적이 없으면)
                q.append(i)         # 인큐
                visited[i] = 1 + visited[t]  # visited[t]에서 하나 더 온거라고 표시
    return 0    # G까지 경로가 없는 경우


T = int(input())
for t in range(T):
    V, E = map(int, input().split())
    # 인접리스트
    adjl = [[] for _ in range(V+1)]
    for i in range(E):
        n1, n2 = map(int, input().split())  # 입력값의 쌍을 읽어내는 방법
        adjl[n1].append(n2)
        adjl[n2].append(n1)     # 화살표(방향)가 없는 무향그래프 -> 양쪽을 서로 연결
    S, G = map(int, input().split())
    # print(S, G)
    # bfs(S, V, G)       # G는 목적지
    print(f'#{t+1} {bfs(S, V, G)}')