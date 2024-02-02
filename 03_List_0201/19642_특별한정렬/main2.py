T = int(input())


def select(arr):
    for i in range(0, len(arr)):
        # min_idx = i
        target_index = i
        for j in range(i, len(arr)):
            # if arr[min_idx] > arr[j]:  # 핵심 로직(오름 내림을 결정함)
            #     min_idx = j
            # 여기서 일반적인 선택정렬이 아니라 인덱스에 따라 오름, 내림을 결정할 것임
            if not i % 2:  # 짝수 의미(나머지가 0일 때)
                if arr[target_index] < arr[j]:  # 핵심 로직(오름차순 정렬)
                    target_index = j
                    arr[i], arr[target_index] = arr[target_index], arr[i]
            else:  # 홀수를 의미
                if arr[target_index] > arr[j]:  # 핵심 로직(내림차순 정렬)
                    target_index = j
                    arr[i], arr[target_index] = arr[target_index], arr[i]
    return arr


for t in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    result = select(arr)
    print(f'#{t+1} {result}')
