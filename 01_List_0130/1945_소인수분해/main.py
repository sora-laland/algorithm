T = int(input())
for tc in range(T):
    N = int(input())
    a, b, c, d, e = 0, 0, 0, 0, 0
    while N % 2 == 0:
        a += 1
        N /= 2
    while N % 3 == 0:
        b += 1
        N /= 3
    while N % 5 == 0:
        c += 1
        N /= 5
    while N % 7 == 0:
        d += 1
        N /= 7
    while N % 11 == 0:
        e += 1
        N /= 11
    print(f'#{tc+1} {a} {b} {c} {d} {e}')
    # print(a, b, c, d, e, N)