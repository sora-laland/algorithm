T = int(input())

# 여러개의 플이일때는 함수로 구현하기
def sol1(arr, neighbor):
    '''
    인덱스를 활용하여 특정한 범의위 합들을 연속적으로 구해주고
    해당 합들의 크기를 비교하여 최대최소 구하기
    '''
    # max_val = 0     # 최대값의 초기값 : 인풋 기준으로 가능한 가장 작은 값
    # min_val = 10000 + 1     # 최소값의 초기값 : 인풋 기준으로 가능한 가장 큰 값
    # 아니면 첫번째 값을 기준으로 삼기
    sum_val = sum(arr[0:neighbor])  # 첫 구간의 합을 구하고 이걸 기준으로 !
    min_val = max_val = sum_val
    # print('min', min_val, 'max', max_val, 'sum', sum_val)
    # for i in range(1, (len(arr) - neighbor + 1)):   # 첫 구간의 합을 최대 최소롤 썼을 경우
    for i in range(0, (len(arr) - neighbor + 1)):
        sum_val = sum(arr[i:i+neighbor])
        min_val = min(min_val, sum_val)
        max_val = max(max_val, sum_val)
        # print('min', min_val, 'max', max_val, 'sum', sum_val)
    return max_val - min_val

def sol2(arr, neighbor):
    sum_val = sum(arr[0:neighbor])  # 첫 구간의 합을 구하고 이걸 기준으로 !
    min_val = max_val = sum_val
    for i in range(neighbor, len(arr)):
        sum_val = sum_val - arr[i - neighbor] + arr[i]  # 가장 왼쪽의 값을 지우고 새로운 값을 넣어줌
        min_val = min(min_val, sum_val)
        max_val = max(max_val, sum_val)
        # print('min', min_val, 'max', max_val, 'sum', sum_val)
    return max_val - min_val



for t in range(1, T+1):
    N, M = map(int, input().split())
    # print(M, N)
    a = list(map(int, input().split()))
    print(a)
    # sol1(a, M)
    print(f'#{t} {sol1(a, M)}')
    print(f'#{t} {sol2(a, M)}')