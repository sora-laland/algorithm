def f(i, k, s):  # s: i-1까지 선택한 원소의 합
    global cnt
    global min_v
    cnt += 1
    if i == k:
        # print(*P)
        if min_v > s:
            min_v = s
    elif s >= min_v:
        return
    else:
        for j in range(i, k):   # P[i]자리에 올 원소 P[j]
            P[i], P[j] = P[j], P[i]     # P[i] <-> P[j]
            f(i+1, k, s+arr[i][P[i]])
            P[i], P[j] = P[j], P[i]     # 교환전으로 복구


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
P = [i for i in range(N)]
print(P)
min_v = 100
cnt = 0
f(0, N, 0)
print(min_v, cnt)

# 이제 백트랙킹을 적용해 가지치기를 해보자
# 경신되기 전의 최소값보다 크다면 그 뒤는 계산할 필요 없음
# 후보군을 고를 때