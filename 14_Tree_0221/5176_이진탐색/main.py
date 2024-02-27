# 이진 탐색 트리에 저장하는 함수 만들기
# 중위순회 방식으로 순회하면서 자료 저장
T = int(input())


def inorder(n):  # n번 노드를 탐색
    # global value
    if n <= N:  # 이 조건을 벗어나는 값은 실행하지 않음
        inorder(2*n)   # 왼쪽자식 호출
        tree[n] = arr.pop()
        inorder(2*n+1)  # 오른쪽자식 호출


for t in range(T):
    N = int(input())
    tree = [0]*(N+1)  # 빈 트리 만들기
    # value = 0

    arr = list(range(N, 0, -1))
    # print(arr)
    inorder(1)
    # print(tree)
    print(f'#{t+1} {tree[1]} {tree[N//2]}')