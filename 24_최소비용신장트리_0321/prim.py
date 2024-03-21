import sys; sys.stdin = open("input.txt")

from heapq import heappush, heappop


def prim(start):
    pq = []
    MST = [0] * V

    # 최소비용
    sum_weight = 0

    # 시작점 추가
    # [기존 BFS] 노드 번호만 관리
    # [Prim] 가중치가 낮으면 먼저 나와야 한다
    # 동시에 두가지 데이터(가중치, 노드번호)를 다뤄야 한다
    heappush(pq, (0, start))

    while pq:
        weight, now = heappop(pq)

        # 방문 했다면 pass
        # BFS는 무조건 방문하지만, Prim은 일단 pq에 넣고 방문 안할수도 있기에!
        # 우선순위 큐의 특성상 더 먼거리로 가는 방법이 큐에 저장되어 있기 때문에
        # 기존에 더 짧은 거리로 방문했다면 pass
        if MST[now] == 1:
            continue

        # 방문처리
        MST[now] = 1
        # 누적합 추가
        sum_weight += weight

        # 갈 수 있는 노드들을 보면서
        for to in range(V):
            # 갈 수 없거나 이미 방문 했다면 pass
            if graph[now][to] == 0 or MST[to]:
                continue

            heappush(pq, (graph[now][to], to))

    print(f'최소비용: {sum_weight}')


V, E = map(int, input().split())
# 인접행렬로 저장
graph = [[0] * V for _ in range(V)]
for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s][e] = w
    # 무방향 그래프
    graph[e][s] = w


prim(0)