import sys; sys.stdin = open("input.txt")


def bfs(start):
    q = [start]
    visited = [0] * 101
    visited[start] = 1

    # 가장 깊은 뎁쓰의 가장 큰 수
    max_num = start
    # 가장 깊은 뎁쓰
    max_depth = 1

    while q:
        now = q.pop(0)

        # 갈 수 있는 곳들
        for to in adj[now]:
            # 이미 방문했다면 pass
            if visited[to]:
                continue

            # 현재 방문 = 이전방문+1 번만에 왔다!
            visited[to] = visited[now]+1

            # 뎁쓰가 더 깊어졌네? => 넘버를 초기화
            # 뎁쓰는 같은데 숫자가 더 크네? => 초기화
            if max_depth < visited[to] or \
                (max_depth == visited[to] and max_num < to):
                max_depth = visited[to]
                max_num = to

            q.append(to)
    return max_num


N, start = map(int, input().split())
graph = list(map(int, input().split()))
adj = [[] for _ in range(101)]
for i in range(0, N, 2):
    s = graph[i]
    e = graph[i+1]
    adj[s].append(e)

r = bfs(start)
print(r)
