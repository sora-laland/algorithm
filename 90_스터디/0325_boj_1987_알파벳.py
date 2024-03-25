import sys; sys.stdin = open("input.txt")


R, C = map(int, input().split())
arr = [input() for _ in range(R)]
st = []
di = [(0, 1), (1, 0), (0, -1), (0, -1)]
visited = [[0] * C for _ in range(R)]
max_length = 0

st.append((0, 0, 1))
path = ''
while st:
    i, j, cnt = st.pop()
    if cnt < len(path):
        path = path[:cnt-1]
    if arr[i][j] not in path:
        path += arr[i][j]

    if max_length <= len(path):
        max_length = len(path)

    for k in range(4):
        ni = i + di[k][0]
        nj = j + di[k][1]
        if not (0<=ni<R and 0<=nj<C):
            continue
        if arr[ni][nj] in path:
            continue
        st.append((ni, nj, cnt+1))

# print(path)
print(max_length)