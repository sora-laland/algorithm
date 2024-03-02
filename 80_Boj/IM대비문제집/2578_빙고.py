import sys; sys.stdin = open("input.txt")

cheolsu = [list(map(int, input().split())) for _ in range(5)]
calling = [list(map(int, input().split())) for _ in range(5)]


def bingo_count(arr):
    cnt = 0
    for _ in range(2):
        for x in range(5):
            if sum(arr[x]) == 0:
                cnt += 1    # 행방향 조사
        arr = list(map(list, zip(*arr)))    # 전치행렬로 만들어서 열방향 조사

    # 대각선 빙고 조사
    cross_sum1 = 0
    cross_sum2 = 0
    for i in range(5):
        for j in range(5):
            if i == j:
                cross_sum1 += arr[i][j]
            if i + j == 4:
                cross_sum2 += arr[i][j]
    if not cross_sum1:
        cnt += 1
    if not cross_sum2:
        cnt += 1
    return cnt  # 빙고 개수 반환


cnt_list = []
for i in range(5):
    for j in range(5):
        for r in range(5):
            for c in range(5):
                if calling[i][j] == cheolsu[r][c]:
                    cheolsu[r][c] = 0
                    cnt = bingo_count(cheolsu)
                    if cnt >= 3:    # 빙고 개수가 3개 이상이 되면
                        cnt_list.append(i*5 + j + 1)  # 몇번째로 부른 숫자인지 기록
                        # break
print(cnt_list[0])
# print(cnt_list.index(3) + 1)
