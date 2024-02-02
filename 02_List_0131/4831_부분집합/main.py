def make_all_subset(arr):
    n = len(arr)
    all_sub = []
    for i in range(1, 1 << n):
        sub = []
        for j in range(n):
            if i & (1 << j):
                sub.append(arr[j])
        all_sub.append(sub)
    return all_sub


A = list(range(1, 13))
T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    all_sub = make_all_subset(A)    # 모든 부분집합을 만들고 여기서 조건에 맞는 값을 찾자
    count = 0                       # 초기값
    for item in all_sub:
        if len(item) == N and sum(item) == K:
            # print(item)
            count += 1              # 하나씩 늘리기
    print(f'#{t+1} {count}')
