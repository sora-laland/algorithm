import sys; sys.stdin = open("input_dij.txt")
from heapq import heappush, heappop

INF = int(1e9)  # 적당히 큰 값
V, E = map(int, input())
start = 0

# 인접 리스트
graph = [[] for _ in range(V)]
# 누적 거리를 저장할 변수
distance = [INF] * V

# 간선 정보 저장
for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s].append([w, e])

def dijkstra(start):
    pq = []

    # 시작점의 weight, 노드 번호를 한번에 저장
    heappush(pq, (0, start))
    # 시작 노드 초기화
    distance[start] = 0

    while pq:
        # pq 라서 웨이트가 작은 애들부터 나오게 됨
        dist, now = heappop(pq)

        # now가 이미 더 짧은 거리로 온적이 있다면 pass
        if distance[now] < dist:
            continue

        # now에서 인접한 다른 노드확인
        for to in graph[now]:
            next_dist = to[0]
            next_node = to[1]

            # 누적 거리 계산
            new_dist = dist + next_dist

            # 이미 더 짧은 거리로 간 경우 pass
            if new_dist >= distance[next_node]:
                continue

            distance[next_node] = new_dist  # 누적거리를 최단거리로 갱신
            heappush(pq, (new_dist, next_node))  # next_node의 인접 노드들을 pq에 추가가