import sys; sys.stdin = open("swea_input.txt")
import heapq

def dijkstra():
    # 2차원 배열
    distances = [[float('inf')] * N for _ in range(N)]
    # 초기화
    distances[0][0] = 0
    pq = [(0, 0, 0)]  # (비용, i, j)

    while pq:
        # 델타 탐색 후 가장 비용이 덜 드는...
        cost, i, j = heapq.heappop(pq)
        if distances[i][j]<j:

            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni = i + di
                nj = j + dj
                if not (0<=ni<N and 0<=nj<N):
                    continue
                h = arr[ni][nj] - arr[i][j]
                next_cost = 1 + max(0, h)



T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]