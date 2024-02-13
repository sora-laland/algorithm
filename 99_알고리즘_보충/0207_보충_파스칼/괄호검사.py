T = int(input())
for t in range(T):
    test_str = input()
    # print(test_str)
    stack = []
    result = 1
    for c in test_str:
        if c == '(' or c == '{':
            stack.append(c)
        if c == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                result = 0
        if c == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                result = 0
    # print(result)
    if not len(stack) and result:
        ans = 1
    else:
        ans = 0
    print(f'#{t+1} {ans}')