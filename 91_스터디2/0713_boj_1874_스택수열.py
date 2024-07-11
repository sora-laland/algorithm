import sys; sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
result = [int(input()) for _ in range(n)]

stack = [0]  #인덱스 에러 방지
asc = 0  # 오름차순으로 push할 수열
ans = []


for i in result:
    while asc < i:
        asc += 1
        stack.append(asc)
        ans.append('+')

        if asc == i:
            stack.pop()
            ans.append('-')

    if asc > i:
        if stack[-1] < i:
            stack.append(0)
            # 위반되는 경우를 구별하기 위해
            break
        while stack[-1] >= i:
            stack.pop()
            ans.append('-')


if len(stack) > 1:
    print('NO')
else:
    for x in ans:
        print(x)