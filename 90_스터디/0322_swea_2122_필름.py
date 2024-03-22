import sys; sys.stdin = open("input.txt")
from collections import deque

D, W, K = map(int, input().split())
plate = [list(map(int, input().split())) for _ in range(D)]

def test(arr):
    result = True
    for j in range(W):
        temp = ''
        for i in range(D):
             temp += str(arr[i][j])
        for m in range(2):
            m_str = str(m) * K
            if m_str in temp:
                # print('yes')
                break
        else:
            # print('no')
            result = False
            break
    return result


arr = plate.copy()

def choice(x, lev, start, D):
    if lev == x:
        result = test(arr)
        if result:
            print('pass')
            return

    for i in range(start, D):
        # A약 주입
        arr[i] = [0] * W
        choice(x, lev+1, i+1, D)
        # 초기화
        arr[i] = plate[i]

        # B약 주입
        arr[i] = [1] * W
        choice(x, lev+1, i+1, D)
        # 초기화
        arr[i] = plate[i]


a = choice(2, 0, 0, D)
# print(a)



# a = test(plate)
# print(a)