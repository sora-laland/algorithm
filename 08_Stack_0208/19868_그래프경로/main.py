def dfs(s, e):
    visited = [0] * 100
    st = []
    visited[s] = 1
    result = 0
    while True:
        for w in adj_l[s]:
            if visited[w] == 0:
                if w == e:  # 인접한 정점이 도착점이라면
                    result = 1
                st.append(s)
                s = w
                visited[w] = 1
                break
        else:  # for 문을 다 돌고 s에 남은 인접 정점이 없으면
            if st:
                s = st.pop()
            else:
                break
    return result


T = int(input())
for t in range(T):
    V, E = map(int, input().split())
    adj_l = [[] for _ in range(V+1)]

    for i in range(E):
        n1, n2 = map(int, input().split())
        adj_l[n1].append(n2)
    S, G = map(int, input().split())

    # print(V, E, adj_l, S, G)

    print(f'#{t+1} {dfs(S, G)}')