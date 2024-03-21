import sys; sys.stdin = open("input.txt")

# 대표자의 인덱스를 생성
def make_set(n):
    parents = [i for i in range(n)]  # 각 원소의 부모를 자신으로 초기화
    rank = [0] * n  # 트리의 깊이(랭크)를 저장
    return parents, rank


def find_set(x):
    if parents[x] == x:
        return x
    return find_set(parents[x])

def union(x, y):
    # 대표자 찾고 일단 같은지 확인
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x != root_y:
        # 랭크를 비교하여 더 높은 트리의 루트를 부모로 설정
        if rank[root_x] < rank[root_y]:
            parents[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parents[root_y] = root_x
        else:
            parents[root_y] = root_x
            rank[root_x] += 1


T = int(input())
for t in range(T):
    print(f'#{t+1}', end=' ')
    N, M = map(int, input().split())
    parents, rank = make_set(N+1)

    arr = list(map(int, input().split()))
    n_arr = []
    for i in range(0, (2*M), 2):
        p = arr[i]
        c = arr[i+1]
        n_arr.append((p, c))
    # n_arr.sort()

    for tup in n_arr:
        union(tup[0], tup[1])

    print(parents)
    for i in range(1, N+1):
        parents[i] = find_set(parents[i])

    cnt = 0
    for i in range(1, N+1):
        if i in parents:

            cnt += 1
    print(cnt)
    print(parents)