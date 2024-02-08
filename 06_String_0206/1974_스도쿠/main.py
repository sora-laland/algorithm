T = int(input())


def count_n(lst):
    set_lst = set(lst)
    if len(set_lst) == len(lst):
        return True  # 중복이 없을 때 True 반환
    else:
        return False


for t in range(T):
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    row_bool = True
    for row in sudoku:
        # print(t+1, count_n(row))
        row_bool &= count_n(row)
    # print(t+1, row_bool)

    col_bool = True
    for j in range(9):
        col = []
        for i in range(9):
            col.append(sudoku[i][j])
        # print(j, col)
        col_bool &= count_n(col)
    # print(t+1, col_bool)

    di = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
    dj = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
    sqr_bool = True
    for i in [1, 4, 7]:
        for j in [1, 4, 7]:
            sqr = []
            for k in range(9):
                ni = i + di[k]
                nj = j + dj[k]
                sqr.append(sudoku[ni][nj])
            # print(t+1, sqr)
            sqr_bool &= count_n(sqr)
    # print(t+1, sqr_bool)

    result = int(row_bool and col_bool and sqr_bool)
    print(f'#{t+1} {result}')