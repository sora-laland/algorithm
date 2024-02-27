T = int(input())


def count_sub(n):
    global cnt
    if left[n]:
        cnt += 1
        count_sub(left[n])
    if right[n]:
        cnt += 1
        count_sub(right[n])
    return cnt


for t in range(T):
    E, N = map(int, input().split())
    left = [0] * (E+2)
    right = [0] * (E+2)
    arr = list(map(int, input().split()))
    for i in range(E):  # 간선의 수 만큼 반복
        parent, child = arr[2*i], arr[2*i+1]
        if left[parent] == 0:
            left[parent] = child
        else:
            right[parent] = child
    cnt = 1     # N번의 자기 자신 노드는 개수에 포함

    # print(count_sub(N))
    print(f'#{t+1} {count_sub(N)}')