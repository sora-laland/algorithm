# 1 ~ 6번까지 노드 존재

# 1. make_set
#  이 때 숫자들은 대표자 인덱스(자기 자신이 대표인 데이터가 리스트로 생성)
def make_set(n):
    return [i for i in range(n)]

# 0번은 버리고 1~6 사용
parent = make_set(7)


# 2. find_set
def find_set(x):
    # 자기 자신이 대표네? 끝
    if parent[x] == x:
        return x
    # 위의 조건이 걸리지 않았다 -> 대표자가 따로 있다
    return find_set(parent[x])

# 3. union
#  이미 연결되어있는 경우 고려해야 함
def union(x, y):
    x = find_set(x)
    y = find_set(y)

    # 이미 같은 집합에 속해있다면(대표자가 같다면) 컨티뉴
    if x == y:
        return

    # 다른 집합이라면 합침
    # 더 작은 루트 노드에 합쳐라
    if x < y:
        parent[y] = x
    else:
        parent[x] = y