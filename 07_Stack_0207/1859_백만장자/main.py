T = int(input())
for t in range(T):
    N = int(input())
    price = list(map(int, input().split())) + [0]

    sell = []
    for i in range(1, N):
        if price[i] > price[i-1] and price[i] > price[i+1]:
            sell.append(i)

    print(sell)  # 판매일의 인덱스
    a = []
    for day in sell:
        buy = 0  # 구매가격
        cnt = 0  # 구매 양
        for i in range(0, day+1):   # 이부분을 이전 day 이후부터 탐색하도록 고쳐 ...
            if price[i] < price[day]:
                buy += price[i]
                cnt += 1
        print('구매일 idx', day, '구매가격', buy, '판매가', cnt*price[day])
        a.append(cnt*price[day] - buy)
    print('판매가 리스트', a)
    print(price)
    print()