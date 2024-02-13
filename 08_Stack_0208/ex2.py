'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''


def dfs(i):  # 시작과 마지막
    visited[i] = 1   # 방문표시
    print(i)
    for w in adjl[i]:
        if visited[w] == 0:
            dfs(w)
    # 재귀는 노드의 수가 많지 않을 때


V, E = map(int, input().split())
visited = [0] * (V+1)
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
dfs(1)