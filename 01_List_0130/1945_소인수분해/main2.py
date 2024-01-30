
# 반복을 줄여서 포문 안에다 넣어보려고 시도는 하였으나 잘...
T = int(input())
for tc in range(T):
    N = int(input())
    # a, b, c, d, e = 0, 0, 0, 0, 0
    ind = [0] * 5
    num = [2, 3, 5, 7, 11]
    for i in range(len(num)):
        while N % num[i] == 0:
            ind[i] += 1
            N /= num[i]
    # while N % 3 == 0:
    #     b += 1
    #     N /= 3
    # while N % 5 == 0:
    #     c += 1
    #     N /= 5
    # while N % 7 == 0:
    #     d += 1
    #     N /= 7
    # while N % 11 == 0:
    #     e += 1
    #     N /= 11
    print(f'#{tc+1} {ind}')
    # print(a, b, c, d, e, N)