import sys; sys.stdin = open("input.txt")
from itertools import combinations


def select_comb(r, c):
    visited = [[0]*N for _ in range(N)]
    visited[r][c:c+M] = [1] * M

    pick_comb = [arr[r][c:c+M]]
    for i in range(N):
        for j in range(N-M+1):
            if 1 in visited[i][j:j+M]:
                continue
            else:
                pick_comb.append(arr[i][j:j+M])
                check_max(pick_comb)
                pick_comb.pop()
    return max_honey


# c는 1 ~ N-M+1 안에서 움직임
def check_max(combs):
    global max_honey
    result = 0
    # 총 두 개의 each
    for each in combs:
        max_combi_sum = 0
        sum_val = 0
        if sum(each) > C:
            for r in range(1, len(each)):
                combination = list(combinations(each, r))
                for honey_set in combination:
                    if sum(honey_set) > C:
                        continue
                    else:
                        combi_sum = 0
                        for honey in honey_set:
                            combi_sum += honey**2
                            max_combi_sum = max(max_combi_sum, combi_sum)

        else:
            for honey in each:
                sum_val += honey**2

        result += max_combi_sum + sum_val
    max_honey = max(max_honey, result)



T = int(input())
for t in range(T):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_honey = 0

    max_ans = 0
    for r in range(N):
        for c in range(N-M+1):
            ans = select_comb(r, c)
            max_ans = max(max_ans, ans)
    print(f'#{t+1}', end=' ')
    print(max_ans)
