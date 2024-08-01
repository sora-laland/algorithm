import sys; sys.stdin = open('input.txt')
input = sys.stdin.readline

T = []
P = []
N = int(input())
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

T += [0]
max_sum = 0
path = []

def func(start):
    global max_sum
    if start + T[start] >= N:
        print(path)
        sum_val = 0
        for idx in path:
            sum_val += P[idx]
        max_sum = max(max_sum, sum_val)
        return

    for i in range(start, N):
        path.append(i)
        if i+T[i] <= N:
            func(i + T[i])
        path.pop()

func(0)
print(max_sum)