T = 10


def postfix(string):
    stack = []
    post = ''
    for tk in string:
        if tk == '+':
            if stack:
                post += stack.pop()
            stack.append(tk)  # push
        else:
            post += tk

    while stack:
        post += stack.pop()

    return post


for t in range(T):
    _ = int(input())
    fx = input()
    postfix_fx = postfix(fx)
    print(postfix_fx)
    # st = []
    # for tk in postfix_fx:
    #     if tk != '+':
    #         st.append(tk)
    #     else:
    #         a = st.pop()
    #         b = st.pop()
    #         st.append(int(a)+int(b))    # 연산된 값을 push
    # print(f'#{t+1} {st[0]}')
