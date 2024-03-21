import sys; sys.stdin = open("swea_input.txt")
from heapq import heappush, heappop
T = int(input())
for t in range(T):
    N, E = map(int, input().split())
    adj = [[] for _ in range(N+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        adj[s].append([w, e])   # 거리(비중)와 도착점 넣기

    # 최소 누적 거리
    dist_lst = [11] * (N+1)
    pq = []

    def dijkstra(start):
        # 시작점 push
        heappush(pq, [0, start])
        # 시작점 거리를 초기화
        dist_lst[start] = 0

        while pq:
            dist, now = heappop(pq)

            # 다음으로 갈 수 있는 곳 탐색해서 큐에 넣기
            for to in adj[now]:
                next_dist = to[0]
                next_node = to[1]

                # 새로운(다음 누적) 거리는 현재 거리 + 다음 노드까지의 거리
                new_dist = dist + next_dist

                # 다음 누적거리가 다음 노드의 최소누적보다 크다면 pass
                if new_dist >= dist_lst[next_node]:
                    continue

                # 새로운 최소 값으로 갱신
                dist_lst[next_node] = new_dist
                # 우선순위 큐에 넣기
                heappush(pq, [new_dist, next_node])

    dijkstra(0)
    print(f'#{t+1} {dist_lst[N]}')