# N, M, K = 2, 2, 1
# arrival = [3, 2]
import sys; sys.stdin = open("1860.txt")
T = int(input())
for t in range(T):
    N, M, K = map(int, input().split())
    arrival = list(map(int, input().split()))
    arrival.sort()
    cnt = 0
    ans = "Possible"
    # M초가 지날때마다 K개 붕어빵
    # boong = x초의 붕어빵 총 개수는 x//M초 * K 개
    # 지금까지 판 개수 : cnt = 0
    # 재고 = 총개수 - cnt

    for x in arrival:
        boong = (x//M) * K
        cnt += 1
        if boong - cnt < 0:
            ans = "Impossible"
            break
    print(f'#{t+1} {ans}')