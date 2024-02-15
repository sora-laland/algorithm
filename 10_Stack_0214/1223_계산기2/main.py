T = 10


def postfix(string):
    stack = []
    post = ''
    # +와 *의 우선순위를 고려해줘야 함 !!! * > + !!!
    for tk in string:
        if tk == '+':
            if stack:
                post += stack.pop()
            stack.append(tk)    # 스택이 비어있으면 그대로 push

        elif tk == '*':     #  elif로 써야함
            if stack and stack[-1] == '*':  # 스택에 *가 있을 때 pop -> push
                post += stack.pop()
            stack.append(tk)    # 스택이 비어있거나 top이 +면 push

        else:
            post += tk  # 피연산자

    while stack:
        post += stack.pop()

    return post


for t in range(T):
    _ = int(input())
    fx = input()
    postfix_fx = postfix(fx)
    print(postfix_fx)

    st = []
    for tk in postfix_fx:
        if tk == '+':
            a = st.pop()
            b = st.pop()
            st.append(int(b)+int(a))  # 연산된 값을 push
        elif tk == '*':
            a = st.pop()
            b = st.pop()
            st.append(int(b)*int(a))
        else:
            st.append(tk)
    print(f'#{t+1} {st[0]}')
