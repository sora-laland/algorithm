T = 10


def in_order(arr, i):
    if arr[i]:
        in_order(arr, child_info[i][0])
        print(arr[i], end='')
        in_order(arr, child_info[i][1])


for t in range(T):
    N = int(input())
    node = [0] * (N+1)
    child_info = [[0, 0] for _ in range(N+1)]
    for n in range(N):
        i, char, *child = input().split()
        i = int(i)
        node[i] = char
        child = list(map(int, child))
        if len(child) == 2:
            child_info[i] = child
        if len(child) == 1:
            child_info[i][0] = child[0]
    print(f'#{t+1}', end=' ')
    in_order(node, 1)
    print()