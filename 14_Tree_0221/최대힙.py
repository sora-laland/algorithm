def enq(n):
    # 완전이진트리는 1차원 리스트로 저장 가능
    # swea 연습 문제는 최소힙
    global last
    last += 1       # 마지막 노드 추가(완전이진트리 유지, 1번부터 삽입)
    h[last] = n     # 마지막 노드에 데이터 삽입
    # 부모>자식 조건을 만족하도록 관리
    c = last    # 부모, 자식 비교를 위해
    p = c//2    # 부모 노드의 번호 구하기
    while p >= 1 and h[p] < h[c]:  # 부모가 있는데, 더 작으면
        h[p], h[c] = h[c], h[p]  # 교환
        c = p   # 부모를 새로운 자식으로 설정해서
        p = c//2    # 그 부모와 다시 비교


def deq():
    global last
    tmp = h[1]   # 루트의 키값 보관
    h[1] = h[last]
    last -= 1   # 마지막 노드 삭제
    p = 1       # 새로 옮기 루트
    c = p*2
    while c<=last:  # 자식이 있으면
        if c+1 <= last and h[c]<h[c+1]:  # 오른쪽 자식이 있고 더 크면
            c += 1
        if h[p] < h[c]:
            h[p], h[c] = h[c], h[p]
            p = c
            c = p*2
        else:
            break
    return tmp


N = 10      # 필요한 노드 수
h = [0]*(N+1)   # 최대 힙
# 입력은 2 5 3 6 4 으로 들어옴
# 완전이진트리 틀을 미리 만들어 둔다고 생각(비어있는 힙)
# 마지막 노드 last = 0
last = 0

enq(2)
enq(5)
enq(3)
enq(6)
enq(4)

while(last>0):
    print(deq())