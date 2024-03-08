import sys; sys.stdin = open("input.txt")

N, M, K = map(int, input().split())
arr = []
for _ in range(K):
    row, col, n, d = map(int, input().split())
    arr.append([row, col, n, d])
# print(arr)

di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, -1, 1]

move_arr = []
for a in range(len(arr)):
    n = arr[a][2]
    d = arr[a][3]
    ni = arr[a][0] + di[arr[a][3]]
    nj = arr[a][1] + dj[arr[a][3]]
    if 0<ni<N-1 and 0<nj<N-1:
        move_arr.append([ni, nj, n, d])
    else:  # 빨간 셀로 갔을 때
        n //= 2
        if d % 2:  # 홀수
            d += 1
        else:  # 짝수
            d -= 1
        move_arr.append([ni, nj, n, d])
move_arr.sort()

for b in range(len(move_arr)-1):
    if move_arr[b][0] == move_arr[b+1][0]:
        if move_arr[b][1]:
            pass
print(move_arr)