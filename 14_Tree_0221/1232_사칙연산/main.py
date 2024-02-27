T = 10


def postorder(n):
    if tree[n]:
        postorder(child_info[n][0])
        postorder(child_info[n][1])
        if tree[n] not in '+-*/':
            st.append(tree[n])
        else:
            a = st.pop()
            b = st.pop()
            if tree[n] == '+':
                result = int(b)+int(a)
                tree[n] = str(result)
            if tree[n] == '-':
                result = int(b)-int(a)
                tree[n] = str(result)
            if tree[n] == '/':
                result = int(b)//int(a)
                tree[n] = str(result)
            if tree[n] == '*':
                result = int(b)*int(a)
                tree[n] = str(result)
            st.append(tree[n])  # 연산 결과를 스택에 넣어줌


for t in range(T):
    N = int(input())
    tree = [0] * (N+1)
    child_info = [[0, 0] for _ in range(N+1)]
    for _ in range(N):
        i, x, *child = input().split()
        i = int(i)
        child = list(map(int, child))
        # print(i, x, child)
        tree[i] = x
        if len(child):  # 자식이 있으면 입력값으로 대체
            child_info[i] = child
    st = []
    postorder(1)    # 1번 노드부터 탐색 시작
    print(f'#{t+1} {tree[1]}')  # 최종 트리의 1번 노드