T = 10


def postfix(string):
    stack = [0]  # 인덱스 에러 방지
    post = ''
    for tk in string:
        if tk == '+' and stack[-1] != '+':
            stack.append(tk)  # push
        else:
            post += tk
    if stack[-1] == '+':
        post += stack.pop()  # pop
    return post


for t in range(T):
    _ = int(input())
    fx = input()
    postfix_fx = postfix(fx)
    st = []
    for tk in postfix_fx:
        if tk != '+':
            st.append(tk)
        else:
            a = st.pop()
            b = st.pop()
            st.append(int(a)+int(b))    # 연산된 값을 push
    print(f'#{t+1} {st[0]}')
