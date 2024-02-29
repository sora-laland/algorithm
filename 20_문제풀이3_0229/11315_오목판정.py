import sys; sys.stdin = open("11315.txt")

di = [-1, 0, 1, 1]
dj = [1, 1, 1, 0]

def is_omok():
    for k in range(4):
        for n in range(1, 5):
            ni = i + di[k] * n
            nj = j + dj[k] * n
            if not (0 <= ni < N and 0 <= nj < N): break
            if arr[ni][nj] == '.': break
        else:
            return True
    return False


T = int(input())
for t in range(T):
    N = int(input())
    arr = [input() for _ in range(N)]
    ans = "NO"
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                if is_omok():
                    ans = "YES"
    print(ans)