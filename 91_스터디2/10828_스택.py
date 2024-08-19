import sys; sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    line = input().split()
    if line[0] == 'push':
        stack.append(line[1])
    if line[0] == 'pop':
        if len(stack):
            print(stack.pop())
        else:
            print(-1)
    if line[0] == 'size':
        print(len(stack))
    if line[0] == 'empty':
        if len(stack):
            print(0)
        else:
            print(1)
    if line[0] == 'top':
        if len(stack):
            print(stack[-1])
        else:
            print(-1)