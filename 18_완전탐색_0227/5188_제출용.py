import sys; sys.stdin = open("5188.txt")
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

path = []
def per(x):
    if x == 2*N-1:
        print(path)
        for k in range(2*N-1):
            ni = i + di[path[k]]
            nj = j + dj[path[k]]
        return

    for i in range(2):
        path.append(i)
        per(x+1)
        path.pop()
per(0)


di = [0, 1]
dj = [1, 0]
