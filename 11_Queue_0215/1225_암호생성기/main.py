from collections import deque

for t in range(10):
    tc = int(input())
    arr = list(map(int, input().split()))

    dq = deque()
    for i in arr:
        dq.append(i)
    # print(q)
    # a = dq.popleft() - 1
    # dq.append(a)

    while dq[-1] != 0:
        for n in range(1, 6):   # 한 사이클
            dq.append(dq.popleft() - n)
            if dq[-1] <= 0:
                dq[-1] = 0
                # print(dq[-1])
                # print(dq)
                break
    # print(dq)
    print(f'#{tc}', *dq)
