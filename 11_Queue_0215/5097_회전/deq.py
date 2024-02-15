from collections import deque
T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    dq = deque(map(int, input().split()))

    for m in range(M):
        a = dq.popleft()
        dq.append(a)
    # print(dq)
    print(f'#{t+1} {dq[0]}')