T = 10


def postfix(string):
    stack = []
    postfix = ''
    for tk in string:
        if tk == '+':
            if stack:
                postfix += stack.pop()
            stack.append(tk)  # push
        else:
            postfix += tk  # 피연산자인 경우 출력

    while stack:
        postfix += stack.pop()

    return postfix


for t in range(T):
    _ = int(input())
    fx = input()
    postfix_fx = postfix(fx)
    st = []
    for tk in postfix_fx:
        if tk == '+':
            a = st.pop()
            b = st.pop()
            st.append(a+b)    # 연산된 값을 push
        else:   # 피연산자라면
            st.append(int(tk))

    print(f'#{t+1} {st[0]}')
