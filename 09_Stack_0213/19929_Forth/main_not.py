T = int(input())
for t in range(T):
    postfix = list(input().split())
    stack = []
    # print(postfix)
    for i in postfix:
        if i in '+-*/' and len(stack) >= 2:
            a = int(stack.pop())
            b = int(stack.pop())
            if i == '+':
                stack.append(b+a)
            elif i == '-':
                stack.append(b-a)
            elif i == '*':
                stack.append(b*a)
            elif i == '/':
                stack.append(b//a)
        elif i == '.':
            result = stack[-1]
        else:
            stack.append(i)
    print(result)
    if len(stack) > 1:
        result = 'error'
    print(stack)
    print(f'#{t+1} {result}')


