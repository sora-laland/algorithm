import sys; sys.stdin=open('input.txt')
input = sys.stdin.readline

N, K = map(int, input().split())
arr = []
for _ in range(N):
    a, *b = map(int, input().split())
    arr.append(b)
    if a == K:
        flag = b

# print(flag)
# arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x:(x[0], x[1], x[2]), reverse=True)

rank = 0
for item in arr:
    rank += 1
    if item == flag:
        break
print(rank)
# print(arr)
