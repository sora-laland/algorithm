# 연속한 1의 개수를 세고 그게 k인지 확인하기
# 1 이면 카운트를 올리다가 0을 만나면 다시 초기화
# 그리고 그 값이 k인지 물어봄
# 단, 0을 만나서 카운트를 !! 초기화하기 전에 !! 그 값이 k인지 먼저 물어봐야함
# 즉 뒤가 0일 때 물어봐서 k 개수(ans)를 늘려야함
# 왜? 개수가 딱 맞는것만 세야함
K = 3
N = 6
arr = [0, 1, 0, 1, 1, 1]
ans, cnt = 0, 0
for i in range(N):
    if arr[i] == 0:
        if cnt == K:
            ans += 1
        cnt = 0
    else:
        cnt += 1
        if i == N-1 and cnt == K:  # 마지막 열에 도착했고 그곳에서 1이 k개일 때
            ans += 1
