import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from heapq import heappush, heappop


V, E = map(int, input().split())
K = int(input())

# 인접리스트 adj
adj = [[] for _ in range(V+1)]
INF = 20000 * 300000
# 누적거리를 저장할 변수
distance = [INF] * (V+1)

for _ in range(E):
    u, v, w = map(int, input().split())
    adj[u].append((w, v))
# print(adj)


# 다익스트라
def dijkstra(start):
    # 우선순위큐
    pq = []
    # 시작점의 노드 번호, 가중치를 한번에 저장
    heappush(pq, (0, start))
    # 시작노드 초기화
    distance[start] = 0

    while pq:
        # pq라서 가중치가 작은 애들부터 나옴
        weight, now = heappop(pq)

        # now가 이미 더 짧은 거리로 온적이 있다면
        if distance[now] < weight:
            continue

        # now에서 인접한 다른 노드 모두 확인(weight가 함께 튜플로 저장되어있음)
        for to in adj[now]:
            next_weight = to[0]
            next_node = to[1]

            # 누적거리 계산
            new_weight = weight + next_weight

            # 이미 더 짧은 거리로 간 경우
            if new_weight >= distance[next_node]:
                continue

            # 누적거리를 최단거리로 갱신
            distance[next_node] = new_weight
            # pq에 push
            heappush(pq, (new_weight, next_node))



dijkstra(K)


for dist in distance[1:]:
    if dist == INF:
        print('INF')
    else:
        print(dist)
