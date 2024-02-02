T = int(input())
for t in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    # print(arr)
    a = sorted(arr)
    # print(a)
    new_sort = [0] * N
    for i in range(N):
        if i < N/2:
            new_sort[2*i+1] = a[i]  # 작은 숫자들은 홀수 인덱스에 순서대로 넣기
        else:
            new_sort[2*(N-i-1)] = a[i]  # 큰 숫자들은 짝수 인덱스에 역순으로 넣기
    print(f'#{t+1}', end=' ')
    print(*new_sort[0:10])
