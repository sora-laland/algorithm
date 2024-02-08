def f(n):
    arr = []
    if n == 0:
        return [1]
    if n == 1:
        return [1, 1]
    else:
        arr.append(1)
        for i in range(1, n):
            arr.append(f(n-1)[i-1]+f(n-1)[i])
        arr.append(1)
        return arr


T = int(input())
for t in range(T):
    N = int(input())

    print(f'#{t+1}')
    for i in range(N):
        result = f(i)
        print(*result)
