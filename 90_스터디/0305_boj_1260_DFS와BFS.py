import sys; sys.stdin = open("input.txt")
input = sys.stdin.readline
from collections import deque

N, M, V = map(int, input().split())
# 인접리스트
adj = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)
visited_dfs = [0] * (N + 1)
visited_bfs = [0] * (N + 1)
# st = []


# dfs 정석
'''
st = []
def dfs_2(v):
    visited[v] = 1
    print(v, end=' ')
    while True:
        for w in adj[v]:
            if visited[w] == 0:
                st.append(v)
                v = w  # 방문
                visited[v] = 1
                print(v, end=' ')
                break   # for w에 대한 break
        else:   # 위에서 for 문을 다 돌았다면 실행, 즉 v에 남은 인접정점이 없다면
            if st:
                v = st.pop()
            else:
                break
'''


#재귀를 이용한 dfs
def dfs(v):
    # 방문 표시
    visited_dfs[v] = 1
    print(v, end=' ')
    for w in sorted(adj[v]):    # 작은 노드번호부터 탐색
        if visited_dfs[w] == 0:
            dfs(w)


def bfs(s):
    q = deque()
    q.append(s)
    visited_bfs[s] = 1
    while q:    # 방문 안한 정점이 있다면 계속됨
        v = q.popleft()
        print(v, end=' ')
        for w in sorted(adj[v]):
            if visited_bfs[w] == 0:
                q.append(w)  # 방문하지 않은 정점이라면 넣어줌
                visited_bfs[w] = 1  # 방문표시


dfs(V)
print()
bfs(V)