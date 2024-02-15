def f(i, k):
    global cnt
    global min_v
    cnt += 1
    if i == k:
        # print(*P)
        s = 0    # 선택한 원소의 합
        for j in range(k):
            s += arr[j][P[j]]   # j행에서 P[j] 열을 구한 경우 합구하기
        if min_v > s:
            min_v = s
    else:
        for j in range(i, k):   # P[i]자리에 올 원소 P[j]
            P[i], P[j] = P[j], P[i]     # P[i] <-> P[j]
            f(i+1, k)
            P[i], P[j] = P[j], P[i]     # 교환전으로 복구


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
P = [i for i in range(N)]
min_v = 100
cnt = 0
f(0, N)
print(min_v, cnt)

# 이제 백트랙킹을 적용해보자
# 경신되기 전의 최소값보다 크다면 그 뒤는 계산할 필요 없음
# 후보군을 고를 때