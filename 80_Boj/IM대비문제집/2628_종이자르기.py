import sys; sys.stdin = open("input.txt")

W, H = map(int, input().split())
width = [0]
height = [0]
N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    if x:   # 세로로 자르는 점선은 width를 가르는 선
        width.append(y)
    else:
        height.append(y)
width.sort()
width.append(W)
height.sort()
height.append(H)

max_width = 0
max_height = 0
for i in range(len(width)-1):
    a = width[i+1] - width[i]
    if a > max_width:
        max_width = a

for j in range(len(height)-1):
    b = height[j+1] - height[j]
    if b > max_height:
        max_height = b

print(max_width * max_height)