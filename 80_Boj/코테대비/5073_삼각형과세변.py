import sys; sys.stdin=open('input.txt')
input = sys.stdin.readline

while True:
    arr = list(map(int, input().split()))
    if arr == [0, 0, 0]:
        break

    # 삼각형의 조건을 만족하지 않음
    if 2 * max(arr) >= sum(arr):
        print("Invalid")
    else:
        flag = 0
        for i in arr:
            flag += arr.count(i)
        if flag == 9:
            print('Equilateral')
        elif flag == 5:
            print('Isosceles')
        else:
            print('Scalene')