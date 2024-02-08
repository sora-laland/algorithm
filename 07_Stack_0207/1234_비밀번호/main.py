T = 10
for t in range(T):
    N, M = input().split()
    # print(N)
    # print(M)
    stack = [0]
    for num in M:
        if num != stack[-1]:
            stack.append(num)
        else:
            stack.pop()
    result = stack[1:(len(M)+1)]
    print(f'#{t+1}', ''.join(result))