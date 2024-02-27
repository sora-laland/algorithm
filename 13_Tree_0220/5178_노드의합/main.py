T = int(input())
for t in range(T):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)
    for _ in range(M):
        n, v = map(int, input().split())
        tree[n] = v  # 리프노드의 값을 번호에 맞게 넣어줌
    # tree를 뒤에서부터 돌면서 부모노드를 구하고 부모노드 인덱스에 해당 값을 더해줌
    for i in range(N, 1, -1):   # 1은 부모노드가 없기 때문에 돌 필요 없음
        parent = i // 2     # i번 노드의 부모노드는?
        tree[parent] += tree[i]
    # print(tree)
    print(f'#{t+1} {tree[L]}')