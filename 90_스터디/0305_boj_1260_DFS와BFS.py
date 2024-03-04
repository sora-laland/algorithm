import sys; sys.stdin = open("input.txt")
N, M, V = map(int, input().split())
# 인접리스트
adjl = [[] for _ in range(N+1)]
# print(adjl)
for _ in range(M):
    x, y = map(int, input().split())
    adjl[x].append(y)
    adjl[y].append(x)
# print(adjl)


visited = [0] * (N+1)
st = []
def dfs(v):
    visited[v] = 1
    while st:
        print(v)
        if visited[adjl[v][0]] == 0:
            st.append(v)
            v = adjl[v][0]  # 방문
            visited[v] = 1
        else:
            if st:
                v = st.pop()
            else:
                break
dfs(1)