import sys; sys.stdin = open("input.txt")
from collections import deque

T = int(input())
for t in range(T):
    n = int(input())
    conv = []
    for _ in range(n+2):
        x, y = map(int, input().split())
        conv.append((x, y))
    home = conv[0]
    # 50미터당 한병 최대 20병이므로
    # 편의점이나 펜타포트로 1000미터 이내라면 갈 수 있음
    # 집 + 편의점 n개 + 마지막 인덱스 페스티벌
    visited = [0]*(n+2)
    queue = deque()
    # 시작점(=집) 인큐
    queue.append(conv[0])
    visited[0] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(1, n+2):
            distance = (abs(conv[i][0] - x) + abs(conv[i][1] - y))
            if visited[i] == 0 and distance <= 1000:
                queue.append(conv[i])
                visited[i] = 1

    if visited[n+1]:
        print('happy')
    else:
        print('sad')