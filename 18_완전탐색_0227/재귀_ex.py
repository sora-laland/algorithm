# for i in range(1, 4):
#     for j in range(1, 4):
#         for k in range(1, 4):
#             for l in range(1, 4):
#                 print(i, j, k, l)

#
# def print_num(n):
#     if n == 6:  # 기저조건
#         return
#     print(n, end=' ')
#     print_num(n+1)
#     print(n, end=' ')
#
#
# print_num(0)
#
#
# def tree(n):
#     if n == 3:
#         return
#     for i in range(2):
#         tree(n+1)
#
#
# tree(0)


def type1(n):
    if n == 3:  # level:3
        print(path)
        return
    for i in range(1, 5):   # branch:4
        path.append(i)  # 경로를 추가
        type1(n+1)    # 재귀호출
        path.pop()  # 이전 레벨로 돌아가면서 해당 레벨의 값을 삭제
# type1(0)


def type2(n):
    if n == 3:  # level:3
        print(path)
        return
    for i in range(1, 5):   # branch:4
        if used[i]:
            continue
        used[i] = True
        path.append(i)  # 경로를 추가
        type2(n+1)    # 재귀호출
        path.pop()  # 이전 레벨로 돌아가면서 해당 레벨의 값을 삭제
        used[i] = False


path = []
used = [False for _ in range(5)]
type2(0)
