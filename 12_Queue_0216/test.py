'''
V E : 1~V번 까지 V개 정점, E개 간선
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''


def bfs(s, N):  # 시작정점 s, 노드개수 N
    q = []                  # 큐
    visited = [0]*(N+1)     # visited,, 맨 앞의 0인덱스는 쓰지 않음
    q.append(s)             # 시작점 인큐
    visited[s] = 1          # 시작점 방문표시
    # 큐가 비워질때까지...(남은 정점이 있으면)
    while q:
        t = q.pop(0)        # 앞에걸 꺼내
        # t에서 할 일...
        print(t)
        for i in adjl[t]:   # t에 인접인 정점 i 꺼내
            if visited[i] == 0:     # 방문하지 않은 정점이면
                q.append(i)         # 인큐
                visited[i] = 1 + visited[t]  # visited[t]에서 하나 더 온거라고 표시
    print(visited)


V, E = map(int, input().split())
arr = list(map(int, input().split()))
# 인접리스트
adjl = [[] for _ in range(V+1)]
for i in range(E):
    n1, n2 = arr[2*i], arr[2*i+1]  # 입력값의 쌍을 읽어내는 방법
    adjl[n1].append(n2)
    adjl[n2].append(n1)     # 화살표(방향)가 없는 무향그래프 -> 양쪽을 서로 연결

bfs(1, V)