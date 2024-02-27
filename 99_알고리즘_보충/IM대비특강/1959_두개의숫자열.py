import sys
sys.stdin = open("1959.txt")

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # 어떤 걸 작은걸로 놓고 할건지? N > M으로 일단 생각
    # 반대의 경우라면 바꿔준다
    if N < M:
        A, B = B, A
        N, M = M, N

    ans = -0xffffffff  # 첫번째 구간에 대한 계산 값이 반드시 저장되도록 초기값 설정
    for s in range(N-M+1):
        # 시작 s, 끝 s+M-1
        val = 0
        for i in range(M):
            val += A[s+i] * B[i]
        if ans < val:
            ans = val
    print(f'#{t+1} {ans}')