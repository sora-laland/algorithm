import sys; sys.stdin = open("input.txt")
from itertools import combinations, permutations


def synergy(A, B):
    A_sum = 0
    B_sum = 0
    for i, j in permutations(A, 2):
        A_sum += table[i-1][j-1]
    for i, j in permutations(B, 2):
        B_sum += table[i-1][j-1]
    return abs(A_sum - B_sum)


T = int(input())
for t in range(T):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    min_val = 20000 * 56
    arr = [n for n in range(1, N+1)]
    for combi in combinations(arr, (N//2)):
        A_ing = list(combi)
        B_ing = list(set(arr) - set(combi))
        temp = synergy(A_ing, B_ing)
        min_val = min(min_val, temp)
    print(f'#{t+1} {min_val}')