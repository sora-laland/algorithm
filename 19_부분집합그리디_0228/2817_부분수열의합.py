import sys; sys.stdin = open("2817.txt")


def get_sub_sum(tar):
    sum_val = 0    # 부분집합 내 원소의 합
    for i in range(N):
        # 1비트가 1인지 확인
        if tar & 0x1:
            sum_val += arr[i]  # 그 자리의 원소가 포함되면 합에 더해준다
            # print(arr[i], end=' ')
        # 오른쪽 끝 비트를 하나씩 제거
        tar >>= 1
    return sum_val


T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    result = 0
    for tar in range(1 << N):  # 2의 n제곱 만큼
        if get_sub_sum(tar) == K:   # 원소의 합이 K 라면
            result += 1
    print(f'#{t+1} {result}')
