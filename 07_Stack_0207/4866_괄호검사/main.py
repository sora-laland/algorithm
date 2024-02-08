T = int(input())
for t in range(T):
    str_ex = input()
    # print(str_ex)

    stack = []
    # result = 0

    result = 1

    # range 벗어날 때 생각
    for i in str_ex:
        if i == '(' or i == '{':
            stack.append(i)
        if stack and i == ')':
            a = stack.pop()
            if a == '{':
                result = 0
                break
        if stack and i == '}':
            a = stack.pop()
            if a == '(':
                result = 0
                break

        if len(stack) == 0:
            result = 1

    print(stack)
    print(f'#{t + 1} {result}')
