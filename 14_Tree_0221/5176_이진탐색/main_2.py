# 스택을 활용한 강사님 풀이
N = int(input())    # 전체 노드의
# 1~N까지 노드들을 배치
num = 1
tree = [0]*(N+1)    # 0, 1~N
order = []  # 중위 순회시 노드 방문 순서
visited = [0]*(N+1)  # 각각 노드에 방문 여부를
st = [1]
# 노드와 값이 다름
while st:
    node = st.pop()
    # 1. 리프 노드일 경우
    # 현재의 노드 번호에 2배 -> 왼쪽 자녀 노드의 번호(이진트리)
    if node*2 > N:
        order.append(node)
        continue
    # 2. 부모노드일 경우(자식이 있을때)
    # - 1. 이미 방문한 부모노드
    # - 2. 새롭게 방문한 부모노드
    if visited[node]:
        order.append(node)
        continue
    # 방문 처리를 하고 본인을 다시 스택에 넣음
    visited[node] = 1
    # 오른쪽 노드를 가장 마지막에 처리
    if node*2+1 <= N:
        st.append(node*2+1)
    st.append(node)  # 부모노드(두번째 방문시)
    # 왼쪽 노드(가장 먼저 처리)
    if node*2 <= N:
        st.append(node*2)
for o in order:
    tree[o] = num
    num += 1    # 인덱스에 따른 for문 구현도...
print(tree[1], tree[N//2])