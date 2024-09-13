import sys; sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort()

for items in arr:
    for item in items:
        print(item, end=" ")
    print()