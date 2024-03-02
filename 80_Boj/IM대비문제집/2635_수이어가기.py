import sys; sys.stdin = open("input.txt")


def number(n1, n2):
    arr = [n1, n2]
    while True:
        new = arr[-2] - arr[-1]
        if new < 0:
            break
        arr.append(new)
    return arr


N1 = int(input())
max_len = 0
for N2 in range(1, N1+1):   # 첫번째 수와 두번째 수가 같을 수도 있음
    arr = number(N1, N2)
    print(arr)
    if len(arr) > max_len:
        max_len = len(arr)
        max_arr = arr
print(max_len)
print(*max_arr)
