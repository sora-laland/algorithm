T = int(input())
for t in range(T):
    postfix = list(input().split())
    stack = []
    # print(postfix)
    for i in postfix:
        if i not in '+-*/.':
            stack.append(i)
        else:
            if i == '.':
                continue
            if len(stack) < 2:
                result = 'error'
                break
            a = int(stack.pop())
            b = int(stack.pop())
            if i == '+':
                stack.append(b+a)
            if i == '-':
                stack.append(b-a)
            if i == '*':
                stack.append(b*a)
            if i == '/':
                stack.append(b//a)
    else:
        if len(stack) == 1:
            result = stack[0]
        else:
            result = 'error'
    #
    # print(stack)
    # print(result)
    print(f'#{t+1} {result}')


