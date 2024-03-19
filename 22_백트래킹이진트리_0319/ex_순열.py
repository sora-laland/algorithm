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

    # 갈 수 있는 후보군
    for i in range(len(arr)):
        # 여기는 못감(가지치기)
        # 백트래킹 코드 팁 : 갈 수 없는 경우에 컨티뉴 활용
        if arr[i] in path:
            continue

        path[level] = arr[i]
        dfs(level + 1)
        # 갔다와서 할 로직 :
        # 기존 방문을 초기화
        path[level] = 0

dfs(0)