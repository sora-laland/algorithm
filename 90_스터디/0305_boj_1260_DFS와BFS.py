import sys; sys.stdin = open("input.txt")
N, M, V = map(int, input().split())
# 인접리스트
adj = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)
visited = [0] * (N+1)
st = []

# dfs 정석
def dfs(v):
    visited[v] = 1
    print(v)
    while True:
        for w in adj[v]:
            if visited[w] == 0:
                st.append(v)
                v = w  # 방문
                visited[v] = 1
                print(v)
                break   # for w에 대한 break
        else:   # 위에서 for 문을 다 돌았다면 실행, 즉 v에 남은 인접정점이 없다면
            if st:
                v = st.pop()
            else:
                break


# 재귀를 이용한 dfs
def dfs_(v):
    # 방문 표시
    visited[v] = 1
    print(v)
    for w in adj[v]:
        if visited[w] == 0:
            dfs_(w)


dfs(1)
print()
# dfs_(1)