import sys; sys.stdin = open("input.txt")

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


def choice(x, lev, start):
    global flag
    if lev == x:
        result = test(arr)

        if result:
            # print('pass', x)
            flag = x
            return

    for i in range(start, D):
        # A약 주입
        arr[i] = [0] * W
        choice(x, lev+1, i+1)
        # 초기화
        arr[i] = plate[i]

        # B약 주입
        arr[i] = [1] * W
        choice(x, lev+1, i+1)
        # 초기화
        arr[i] = plate[i]


# a = choice(1, 0, 0)
# print(a)
T = int(input())
for t in range(T):
    print(f'#{t+1}', end=' ')
    D, W, K = map(int, input().split())
    plate = [list(map(int, input().split())) for _ in range(D)]
    arr = plate.copy()
    flag = 0

    if test(arr):
        print(0)
    else:
        for x in range(1, D+1):
            choice(x, 0, 0)
            if flag:
                print(flag)
                break
