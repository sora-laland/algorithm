T = int(input())
for t in range(T):
    N = int(input())
    counts = [0] * 5001  # 5000개의 정류장
    # 정류장
    for i in range(N):
        A, B = map(int, input().split())
        for j in range(A, B+1):  # A < B 인 조건이 있었기에
            counts[j] += 1
    P = int(input())
    bus_stop = [int(input()) for _ in range(P)]
    print(f'#{t+1}', end=' ')
    for i in bus_stop:
        print(counts[i], end=' ')
    print()
