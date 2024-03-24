import sys; sys.stdin = open("input.txt")

R, C = map(int, input().split())
arr = [input() for _ in range(R)]
st = []
di = [(0, 1), (1, 0), (0, -1), (0, -1)]
# visited = [[0] * C for _ in range(R)]


st.append((0, 0))
path = ''
while st:
    i, j = st.pop()
    path += arr[i][j]
    for k in range(4):
        ni = i + di[k][0]
        nj = j + di[k][1]
        if not (0<=ni<R and 0<=nj<C):
            continue
        if arr[ni][nj] in path:
            continue
        st.append((ni, nj))
print(path)