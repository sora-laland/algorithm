import sys; sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

count_5 = N // 5 + 1
count_3 = 0

while True:
    if count_5 < 0:
        ans = -1
        break
    if count_5 * 5 + count_3 * 3 == N:
        ans = count_5 + count_3
        break

    count_5 -= 1
    count_3 = (N - count_5 * 5) // 3

print(ans)