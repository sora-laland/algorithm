import sys; sys.stdin=open('input.txt')
input = sys.stdin.readline
H, W, N, M = map(int, input().split())

# 가로 방향으로 몇개??
hor = W // (M+1)
if W % (M+1):
    hor += 1

ver = H // (N+1)
if H % (N+1):
    ver += 1

print(hor * ver)