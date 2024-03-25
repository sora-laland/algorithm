import sys; sys.stdin = open("input.txt")

sys.setrecursionlimit(10**9)
R, C = map(int, input().split())
arr = [input() for _ in range(R)]
di = [(0, 1), (1, 0), (-1, 0), (0, -1)]
max_length = 0
# path = set()

#
# def dfs(i, j, cnt):
#     global max_length
#     max_length = max(max_length, cnt)
#     for k in range(4):
#         ni = i + di[k][0]
#         nj = j + di[k][1]
#         if not (0<=ni<R and 0<=nj<C):
#             continue
#         if arr[ni][nj] in path:
#             continue
#         path.add(arr[ni][nj])
#         dfs(ni, nj, cnt+1)
#         path.remove(arr[ni][nj])
st = set()
st.add((0, 0, 1))
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
        st.add((ni, nj, cnt+1))

# print(path)
print(max_length)


# path.add(arr[0][0])
# dfs(0, 0, 1)
# print(max_length)
