import sys
sys.stdin = open("3499.txt")

T = int(input())
for t in range(T):
    print(f'#{t+1}', end=' ')
    N = int(input())
    arr = list(input().split())
    # print(arr)
    front = 0
    mid = N // 2
    if N % 2:
        mid += 1
    for i in range(N//2):
        print(arr[front], end=' ')
        front += 1
        print(arr[mid], end=' ')
        mid += 1
    print()