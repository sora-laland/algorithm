import sys; sys.stdin = open("input.txt")

N = int(input())
arr = list(map(int, input().split()))


def switch_boy(n):
    for i in range(n-1, N, n):
        arr[i] = abs(arr[i] - 1)  # 스위치의 상태를 바꿈 : -1을 하고 절대값


def switch_girl(n):
    arr[n-1] = abs(arr[n-1] - 1)
    for i in range(1, N//2):
        if (n-1)-i < 0 or (n-1)+i >= N:  # 범위를 벗어나면 break
            break
        if arr[(n-1)-i] == arr[(n-1)+i]:
            arr[(n-1)-i] = abs(arr[(n-1)-i] - 1)    # 스위치 상태를 바꿈
            arr[(n-1)+i] = abs(arr[(n-1)+i] - 1)
        else:
            break


stN = int(input())
for _ in range(stN):
    sex, number = map(int, input().split())
    if sex == 1:
        switch_boy(number)
    else:
        switch_girl(number)

for i in range(N):
    if (i+1) % 20 == 0:     # 20개씩 끊어서 출력
        print(arr[i], end=' ')
        print()
    else:
        print(arr[i], end=' ')