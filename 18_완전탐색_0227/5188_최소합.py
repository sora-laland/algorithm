import sys; sys.stdin = open("5188.txt")


# 시간초과를 방지하기 위해 가지치기 필요
# 누적합으로 가지치기
# 중간의 누적합이 최소값보다 크다면 그 경로는 더이상 탐색하지 않는다
def dfs(i, j, cum_sum):
    # print(i, j)
    cum_sum += matrix[i][j]
    if i == j == N-1:   # 목표에 도달
        global min_value
        min_value = min(cum_sum, min_value)
    # 불필요한 dfs 호출을 막아주기 위해 가지치기
    if cum_sum >= min_value:
        # 이전에 진행되었던 재귀 호출의 결과물보다 현재 누적합이 크다면
        # 현재 누적합이 크거나 같다면
        return  # 뒤에 dfs 호출을 차단
    # 오른쪽과 아래를 탐색
    di = [1, 0]
    dj = [0, 1]
    for ii in range(2):
        ni = i + di[ii]
        nj = j + dj[ii]
    # i 나 j가 범위를 넘는지 확인
        if not (0<=ni<N):
            continue
        if not (0<=nj<N):
            continue
            # 인덱스오류 방지
        dfs(ni, nj, cum_sum)


T = int(input())
for t in range(T):
    print(f'#{t+1}', end=' ')
    N = int(input())
    matrix = [list(map(int, input().split()))
              for _ in range(N)]
    # 지나가는 칸의 수 : 2N-1, 한 칸당 최대값: 10
    min_value = (2 * N-1) * 10  # 최소값 지정
    # 이거를 갱신할 것
    # 1. 이것만 갱신할 때 -> min_value = min(new_value, min_value)
    # 2. 조건문 -> 얘랑 동시에 다른 애도 바꿔줘야할 때
    dfs(0, 0, 0)    # 시동걸기(초기값 고정)
    print(min_value)
