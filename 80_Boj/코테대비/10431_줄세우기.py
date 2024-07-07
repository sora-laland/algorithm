import sys; sys.stdin=open('input.txt')
input = sys.stdin.readline

P = int(input())
for _ in range(P):
    P, *arr = map(int, input().split())
    # print(P)
    # print(arr)
    ans = 0
    for i in range(1, 20):
        for x in range(i):
            if arr[x] > arr[i]:
                ans += 1
    print(P, ans)

