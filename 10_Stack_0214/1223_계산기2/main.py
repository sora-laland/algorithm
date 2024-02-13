T = 10


def postfix(string):
    stack = [0]  # 인덱스 에러 방지
    post = ''
    # +와 *의 우선순위를 고려해줘야 함 !!! * > + !!!
    for tk in string:
        if tk in '+*' and stack[-1] not in '+*':
            stack.append(tk)  # push
        else:
            post += tk
    if stack[-1] in '+*':
        post += stack.pop()  # pop
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
