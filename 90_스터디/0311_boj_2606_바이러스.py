import sys; sys.stdin = open("input.txt")

N = int(input())
M = int(input())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, (input().split()))
    adj[a].append(b)
    adj[b].append(a)


cnt = 0
for end in range(2, N+1):
    visited = [0]*(N+1)
    st = [1]    # 1에서 시작
    while st:
        v = st.pop()
        if visited[v] == 0:
            visited[v] = 1
            for node in adj[v]:
                st.append(node)
        if v == end:
            cnt += 1
            break   # 경로를 하나 찾으면 break
print(cnt)