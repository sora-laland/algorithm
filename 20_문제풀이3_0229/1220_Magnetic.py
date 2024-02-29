import sys; sys.stdin = open("1220.txt")
T = 10
for t in range(T):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(100)]
    total_cnt = 0

    # 열검사 함수
    def get_sero_cnt(col):
        cnt = 0
        is_red = False

        for i in range(100):
            # 1. 레드 발견
            if table[i][col] == 1:
                is_red = True
            # 2. 이전에 레드고 현재 블루를 발견했다면
            # -> 이미 레드가 한번 이상 나온 상태에서 블루가 나온것이라면
            elif is_red and table[i][col] == 2:
                cnt += 1
                is_red = False  # 갱신, 다음에 새로 레드가 나올때까지 교착은 일어나지 않는다
        return cnt


    for col in range(N):
        total_cnt += get_sero_cnt(col)
    print(f'#{t+1} {total_cnt}')