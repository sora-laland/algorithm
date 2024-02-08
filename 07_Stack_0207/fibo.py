def fibo(n):
    global cnt
    cnt += 1    # 호출시마다 카운트
    if n < 2:  # 종료상황 만들어줘야 한다
        return n
    else:
        return fibo(n-1) + fibo(n-2)


def fibo_memo(n):
    global cnt
    cnt += 1
    if n != 0 and memo[n] == 0:  # 0이 아닌데 값이 비어있는 경우
        memo[n] = fibo_memo(n-1) + fibo_memo(n-2)
    return memo[n]


cnt = 0
n = 7
print(fibo(n), cnt)

cnt = 0  # 다시 초기화
memo = [0]*(n+1)
memo[0] = 0
memo[1] = 1     # 초기값 미리 설정
print(fibo_memo(n), cnt)