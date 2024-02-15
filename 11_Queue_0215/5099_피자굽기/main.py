from collections import deque

N, M = map(int, input().split())
pizzas = list(map(int, input().split()))

oven = deque()
for i in range(N):
    oven.append(i)  # 피자의 인덱스
# print(oven)

end = 0 # 몇번째 피자까지 썼는지 인덱스에 더해줄 값
while oven:
    for i in range(N):
        print(pizzas)
        front = oven.popleft()
        pizzas[front] //= 2
        oven.append(front)
        print(front, oven)
        if pizzas[front] == 0:
            oven[0] = N+end
            end += 1
        print(pizzas)
        print()



        # if check == 0:
        #     oven.pop()
        #     if N+end < M:
        #         oven.append(Ci[N+end])
        #         end += 1    # 피자가 남았는지 확인
