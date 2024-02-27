import sys
sys.stdin = open("10580.txt")


def get_result():
    size = len(arr)
    cnt =0
    for i in range(size):
        for tar in range(i):
            i_a, i_b = (arr[i][0], arr[i][1])
            tar_a, tar_b = (arr[tar][0], arr[tar][1])
            if i_b < tar_b:
                cnt += 1
    return cnt


T = int(input())
for t in range(T):
    N = int(input())
    arr = []
    for _ in range(N):
        a, b = map(int, input().split())
        arr.append((a, b))
        # 함수 호출 이전에 정렬 필요

    arr.sort(key = lambda x : x[0])  # 첫번째 원소 기준으로 오름차순 정렬
    result = get_result()
    print(f'#{t+1} {result}')