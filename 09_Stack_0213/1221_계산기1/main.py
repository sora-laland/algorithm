T = 10


def postfix(string, n):
    stack = [0] * n
    post = ''
    top = -1
    for tk in string:
        if tk == '+' and stack[top] != '+':
            top += 1
            stack[top] = tk  # push
        elif tk == '+':
            top -= 1
            post += stack[top+1]    # pop해서 post에 붙임
            top += 1                # +를 다시 스택에 push
            stack[top] = tk
        else:
            post += tk
    if stack[top] == '+':
        post += stack[top]
    return post


for t in range(T):
    N = int(input())
    fx = input()
    postfix_fx = postfix(fx, N)
    st = []
    for tk in postfix_fx:
        if tk != '+':
            st.append(tk)
        else:
            a = st.pop()
            b = st.pop()
            st.append(int(a)+int(b))    # 연산된 값을 push
    print(f'#{t+1} {st[0]}')


