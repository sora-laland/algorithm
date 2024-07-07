import sys; sys.stdin=open('input.txt')
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x:(x[1], x[2], x[3]), reverse=True)

print(arr)