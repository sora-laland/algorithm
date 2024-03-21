# 인접 행렬 DFS
graph_m = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 0, 0],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0],
]

visited = [0] * 5
path = []

# 스택이 아닌 재귀로 구현해보자
def dfs(now):
    # 기저 조건
    # 지금 문제에선 없다

    # 다음 재귀 호출 전
    # 여기에 적으면 재귀 호출 후에 실행하는 것
    # visited[now] = 1
    # path.append(now)

    # 다음 재귀 호출
    # dfs에선 현재 노드에서 다른 노드들을 확인
    # 다른 노드'들' -> 반복문
    for to in range(5):
        # 갈 수 없다면 pass
        if graph_m[now][to] == 0:
            continue
        # 이미 방문했다면 pass
        if visited[to] == 1:
            continue

        # 이걸 여기에 적어주면 가기 전에 작업
        visited[to] = 1
        path.append(to)

        dfs(to)

    # 돌아왔을 때 작업


# 함수 호출 전에 초기화
visited[0] = 1
path.append(0)

dfs(0)
print(path)