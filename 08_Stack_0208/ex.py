'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''


def dfs(i, V):  # 시작과 마지막
    # visited, stack 생성 및 초기화
    st = []
    visited = [0] * (V+1)
    visited[i] = 1  # 시작점 방문
    print(i)    # 방문한 정점번호 출력
    while True:  # 탐색
        # 현재에서 인접하고 방문 안한 정점 w가 있으면
        for w in adjl[i]:   # 인접한 정점 중
            if visited[w] == 0:     # 방문하지 않은 곳이라면?
                st.append(i)    # i를 지나서 방문했다는 정보
                i = w   # w에 방문
                visited[i] = 1
                print(i)
                break   # for w
        else:                   # for w, i에 남은 인접 정점이 없으면
            # 스택이 비어있지 않으면(=지나온 정점이 있으면)
            if st:
                i = st.pop()
            else:   # 스택이 비어있으면(=출발점이면)
                break   # while True


V, E = map(int, input().split())
arr = list(map(int, input().split()))
# 입력값을 인접 리스트로 받기
# 0번 인덱스는 무시
adjl =[[] for _ in range(V+1)]
for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    # 방향이 없는 경우 -> 양쪽을 다 생각
    # 방향을 생각하는 건 데이터를 저장할 때 !
    adjl[n1].append(n2)
    adjl[n2].append(n1)
# print(adjl)
dfs(1, V)