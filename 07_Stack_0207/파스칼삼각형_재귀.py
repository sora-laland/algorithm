def f(n):
    arr = []
    if n == 0:
        # print([1])
        return [1]
    if n == 1:
        # print([1, 1])
        return [1, 1]
    else:
        arr.append(1)
        for i in range(1, n):
            arr.append(f(n-1)[i-1]+f(n-1)[i])
        arr.append(1)
        # print(arr)
        return arr

f(0)
f(1)
f(2)
f(3)
f(4)

# T = int(input())
# for t in range(T):
#     N = int(input())
#
#     print(f'#{t+1}')
#     for i in range(N):
#         result = f(i)
#         print(*result)
