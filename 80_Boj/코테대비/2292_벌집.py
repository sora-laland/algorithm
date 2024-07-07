import sys; sys.stdin=open('input.txt')
input = sys.stdin.readline

N = int(input())
# print(N)
ans = (N-2) // 6
# print(ans)
n = 1
while True:
    if ans < n * (n+1) / 2:
        break
    else:
        n += 1

if N == 1:
    print(1)
else:
    print(n+1)