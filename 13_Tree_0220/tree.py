'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''


def pre_order(T):
    if T:
        print(T)
        pre_order(left[T])
        pre_order(right[T])


N = int(input())
E = N-1     # 간선 수
arr = list(map(int, input().split()))
left = [0]*(N+1)    # 부모를 인덱스로 왼쪽자식 저장
right = [0]*(N+1)
par = [0]*(N+1)     # 자식을 인덱스로 부모 저장

for i in range(E):
    p, c = arr[2*i], arr[2*i+1]
    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c
    par[c] = p

c = N
while par[c] != 0:  # 부모가 있으면
    c = par[c]      # 부모를 새로운 자식으로 두고
root = c
# print(root)
pre_order(root)