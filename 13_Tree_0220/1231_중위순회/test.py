def in_order(arr, i):
    if arr[i]:
        if child_info[i][0]:
            in_order(arr, child_info[i][0])
        print(arr[i])
        if child_info[i][1]:
            in_order(arr, child_info[i][1])


node = [0, 'W', 'F', 'R', 'O', 'T', 'A', 'E', 'S']
child_info = [0, [2, 3], [4, 5], [6, 7], [8, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
# child_info = [0, [2, 3], [4, 5], [6, 7], [8], [], [], [], []] # 그대로 붙였을 때

# for t in range(T):
#     N = int(input())
#     node = [0] * (N+1)
#     child_info = [0] * (N+1)
#     for n in range(N):
#         i, char, *child = input().split()
#         # print(i, char, child)
#         node[int(i)] = char
#         child = list(map(int, child))
#         child_info[int(i)] = child
#     print(node)
#     print(child_info)

in_order(node, 1)