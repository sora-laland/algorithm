import sys; sys.stdin = open('input.txt')
input = sys.stdin.readline
from itertools import combinations
from collections import deque
arr = [input().rstrip() for _ in range(5)]

"""
1. 25명 중 7명을 뽑는 조합
2. 그 중 이다솜파 4명 이상인지 확인
3. BFS로 가로세로 인접인지 확인
"""

# 상하좌우
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

graph_index = []
for i in range(5):
    for j in range(5):
        graph_index.append((i, j))
print(graph_index)

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
def check_connect(combi):

    combi_arr = [[0]*5 for _ in range(5)]
    for (i, j) in combi:
        combi_arr[i][j] = 1

    return bfs(combi[0], combi_arr)


def bfs(start, combi_arr):
    visited = [[0]*5 for _ in range(5)]
    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] = 1
    cnt = 1

    while queue:
        i, j = queue.popleft()

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni < 0 or ni >= 5:
                continue
            if nj < 0 or nj >= 5:
                continue
            if combi_arr[ni][nj] == 0:
                continue
            if visited[ni][nj] > 0:
                continue
            # 모든 조건 만족
            visited[ni][nj] = 1
            cnt += 1

            if cnt == 7:
                return True

            queue.append((ni, nj))
    return False


# ans = check_lds_4([(1, 0)])
# print(ans)

# a_arr = [[1, 1, 1, 1, 1], [0, 1, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 1]]
# print(bfs((0, 4), a_arr))



ans = 0
for combi in combinations(graph_index, 7):
    if check_lds_4(combi):
        if check_connect(combi):

            print(combi)
            ans += 1

print(ans)