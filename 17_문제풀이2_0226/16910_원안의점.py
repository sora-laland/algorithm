import sys
sys.stdin = open("16910.txt")
T = int(input())
for t in range(T):
    N = int(input())
    cnt = 0
    for x in range(-N, N+1):
        for y in range(-N, N+1):
            if x**2 + y**2 <= N**2:
                cnt += 1
    print(f'#{t+1} {cnt}')