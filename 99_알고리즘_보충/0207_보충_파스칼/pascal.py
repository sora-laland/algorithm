T = int(input())
for t in range(T):
    n = int(input())
    arr = [[1]]
    for i in range(1, n):
        arr.append([])
        arr[i].append(1)

        # 앞 뒤로 1을 붙여주고, 가운데 원소
        for j in range(1, i):
            arr[i].append(arr[i-1][j-1] + arr[i-1][j])

        arr[i].append(1)

    print(f'#{t+1}')
    # print(arr)
    for i in range(n):
        print(*arr[i])