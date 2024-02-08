T = int(input())
for t in range(T):
    str_ex = input()
    stack = [0]

    for i in str_ex:
        if stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)

    print(f'#{t+1}', len(stack)-1)
