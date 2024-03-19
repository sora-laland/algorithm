# 중복순열

arr = [i for i in range(1, 4)]
path = [0] * 3

def dfs(level):
    # 기저 조건
    # 이 문제에선 3개를 뽑았을 때 까지 반복
    if level == 3:
        print(*path)
        return

    # 들어가기 전
    # 다음 재귀를 호출
    #   - 다음에 갈 수 있는 곳들은 어디인가?
    #   - 이 문제에서는 1, 2, 3 세가지(길이만큼) 경우의 수가 존재

    #기본 코드
    # path[level] = 1  # 가기 전에 기록
    # dfs(level + 1)   # 다음 레벨 호출
    #
    # path[level] = 2
    # dfs(level + 1)
    #
    # path[level] = 3
    # dfs(level + 1)

    for i in range(len(arr)):
        path[level] = arr[i]
        dfs(level + 1)

dfs(0)