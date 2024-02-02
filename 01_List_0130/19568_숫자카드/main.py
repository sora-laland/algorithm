T = int(input())
for t in range(T):
    N = int(input())
    card = int(input())
    c = [0] * 10  # 0 ~ 9 까지 정수 10개
    for _ in range(N):  # 단순히 N번 반복할거고
        c[card % 10] += 1  # 10으로 나눈 나머지를(맨 뒷 숫자부터) 계속 카운트 올려줌
        card //= 10
    max_value = max(c)  # 가장 많은 장수(카운트 배열의 max)
    max_card = 0    # 초기값
    for i in range(10):
        if c[i] == max_value:   # 해당 카드의 장수가 최대값이면 초기값을 업데이트
            max_card = i
    # print(c)
    print(f'#{t+1} {max_card} {max_value}')
