import sys; sys.stdin = open('input.txt')
input = sys.stdin.readline
from itertools import combinations
from collections import deque

arr = [input().rstrip() for _ in range(5)]

# 상하좌우
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

graph_index = []
for i in range(5):
    for j in range(5):
        graph_index.append((i, j))
print(graph_index)
"""
1. 25명 중 7명을 뽑는 조합
2. 그 중 이다솜파 4명 이상인지 확인
3. BFS로 가로세로 인접인지 확인
"""
# for combi in combinations(range(25), 7):
    # print(combi)

# 이다솜파 4명인지 확인
def check_lds_4(combi):
    cnt = 0
    for (i, j) in combi:
        if arr[i][j] == 'S':
            cnt += 1
        if cnt >= 1:
            return True
    return False

# 첫번째 자리에서 모든 자리가 bfs로 연결되었는가?
def check_connect(start, combi):

    blank_arr = [[0]*5 for _ in range(5)]
    visited = [[0]*5 for _ in range(5)]
    for (i, j) in combi:
        blank_arr[i][j] = 1

    for item in combi:
        pass

def bfs(start, blank_arr, visited):
    queue = deque(start)
    visited[start[0]][start[1]] = 1

    while queue:
        now = queue.popleft()

        for k in range(4):
            ni = now[0] + di[k]
            nj = now[1] + dj[k]
            if ni < 0 or ni >= 5:
                continue
            if nj < 0 or nj >= 5:
                continue
            if blank_arr[ni][nj] == 0:
                continue
            if visited[ni][nj] == 1:
                continue
            # 모든 조건 만족
            visited[ni][nj] = 1
            queue.append((ni, nj))


ans = check_lds_4([(1, 0)])
print(ans)