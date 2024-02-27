import sys; sys.stdin = open("5189.txt")

T = int(input())

path = [1]
def perm(x):
    if x == N-1:  # 2~N 까지의 관리구역(N-1개)
        # path.append(1)
        # print(path)
        cum_sum = 0
        for p in range(len(path)-1):
            s = path[p] - 1
            e = path[p+1] - 1
            cum_sum += battery[s][e]
        cum_sum += battery[path[-1]-1][0]   # 마지막 경로는 항상 1로 돌아감
        global min_val
        min_val = min(cum_sum, min_val)
        return

    for i in range(2, N+1):  # 2~N 까지의 관리구역을 원소로 순열 만들기
        # 중복x -> 이미 path에 있으면 다음 경로로 선택하지 않음
        if i in path:
            continue
        path.append(i)
        perm(x+1)   # 재귀호출
        path.pop()

for t in range(T):
    N = int(input())
    battery = [list(map(int, input().split())) for _ in range(N)]
    min_val = 100*N
    perm(0)
    print(f'#{t+1} {min_val}')