T = int(input())


def binary(total, target):
    count = 0
    l = 1
    r = total
    while True:
        count += 1
        c = (l + r) // 2  # 중간값
        if c == target:
            break
        elif c < target:
            l = c
        else:
            r = c
    return count


for t in range(T):
    P, A, B = map(int, input().split())
    A_count = binary(P, A)
    B_count = binary(P, B)
    result = 0
    if A_count > B_count: result = 'B'
    if A_count < B_count: result = 'A'

    print(f'#{t+1} {result}')