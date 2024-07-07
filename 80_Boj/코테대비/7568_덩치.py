import sys; sys.stdin=open('input.txt')
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    rank = 1
    x, y = arr[i][0], arr[i][1]
    for item in arr:
        if x < item[0] and y < item[1]:
            rank += 1
    print(rank, end=' ')