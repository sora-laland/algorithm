import sys; sys.stdin = open("input.txt")

def dfs(cnt, sum_height):
    global ans
    # 기저조건
    # B 이상이면 종료
    if sum_height >= B:
        ans = min(ans, sum_height)
        return
    # 모든 점원이 탑을 쌓는데에 고려가 되었다면 종료
    if cnt == N:
        return
    # 쌓는다
    dfs(cnt+1, sum_height+arr[cnt])
    # 안쌓는다
    dfs(cnt+1, sum_height)

T = int(input())
for t in range(T):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = int(1e9)
    dfs(0, 0)
    print(f'#{t+1} {abs(ans-B)}')