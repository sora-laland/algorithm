'''
6
7 2 5 3 4 6
'''
T = int(input())
for t in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    heap = [0] * (N+1)
    last = 0
    for i in arr:
        last += 1
        heap[last] = i
        c = last
        p = c//2
        while p >= 1 and heap[c] < heap[p]:  # 부모가 존재하는데, 만약 부모가 자식보다 크다면 자리를 바꿔줌
            heap[c], heap[p] = heap[p], heap[c]
            # 부모를 새로운 자식으로 할당하고 새로운 p를 지정
            c = p
            p = c//2    # 새로운 부모 노드번호 -> 반복
    # 이진최소힙 생성 완
    # print(heap)
    anc_sum = 0
    parent_node = N // 2
    while parent_node > 0:  # 존재하는 모든 부모노드에 대해
        anc_sum += heap[parent_node]
        parent_node //= 2
    print(f'#{t+1} {anc_sum}')