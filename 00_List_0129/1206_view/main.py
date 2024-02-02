T = 10
for t in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    print(arr)

    count = 0
    for i in range(2, len(arr)-2):
        max_height = max(arr[i-2], arr[i-1], arr[i+1], arr[i+2])
        view = arr[i] - max_height
        if view > 0:
            count += view
    print(f'#{t+1} {count}')
