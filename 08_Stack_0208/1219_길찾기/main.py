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


T = 10
for t in range(T):
    tc_num, N = map(int, input().split())
    arr = list(map(int, input().split()))
    adj_l = [[] for _ in range(100)]

    for i in range(len(arr)//2):
        n1 = arr[2*i]
        n2 = arr[2*i+1]
        adj_l[n1].append(n2)  # 단방향이므로 n1에만 append

    # 같은 코드
    # for i in range(0, len(arr), 2):
    #     adj_l[arr[i]].append(arr[i+1])

    print(f'#{tc_num} {dfs(0, 99)}')