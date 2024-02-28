import sys; sys.stdin = open("5948.txt")

T = int(input())
for t in range(T):
    arr = list(map(int, input().split()))
    N = 7
    # 7개에서 3개를 중복되지 않게 선택(조합)
    sum_lst = []
    for a in range(7):
        for b in range(a+1, 7):
            for c in range(b+1, 7):
                sum_val = arr[a] + arr[b] + arr[c]
                if sum_val not in sum_lst:
                    sum_lst.append(sum_val)  # 중복제거
    sum_lst.sort(reverse=True)
    print(f'#{t+1} {sum_lst[4]}')   # 5번째로 큰 수