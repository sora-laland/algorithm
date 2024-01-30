T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, list(input())))  # 데이터를 하나씩 끊어서 누적합
    print(data)
    # for i in data:



    # count = [0] * N
    # for i in range(1, N):
    #     data[i] = data[i] + data[i-1]
    # print(data)
