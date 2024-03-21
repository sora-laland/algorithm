import sys; sys.stdin = open("input.txt")

def find_set(x):
    if parents[x] == x:
        return x
    # 경로 압축
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if x == y:
        return
    if x < y:
        parents[y] = x
    else:
        parents[x] = y


V, E = map(int, input().split())
edges = []  # 간선 정보들을 모두 저장
for _ in range(E):
    s, e, w = map(int, input().split())
    edges.append([s, e, w])
edges.sort(key=lambda x: x[2])  # 가중치를 기준으로 정렬
parents = [i for i in range(V)]  #대표자 배열

# MST 완성 : 간선의 개수가 V-1이 될 때
cnt = 0
sum_weight = 0

# 간선들을 모두 확인한다
for s, e, w in edges:
    # 사이클이 발생하면 pass
    # union-find에서 이미 같은 집합에 속해있다면
    # 즉 대표자가 같다면 pass
    if find_set(s) == find_set(e):
        print(s, e, w, ' / 사이클 발생 탈락!')
        continue

    print(s, e, w)
    cnt += 1

    # 사이클이 없다면, 방문 처리
    union(s, e)
    sum_weight += w

    if cnt == V - 1:    # MST 완성! 간선의 개수 == V-1
        break

print(f'최소비용: {sum_weight}')