T = int(input())  # 테스트 케이스의 수를 입력받습니다.
A = list(range(1, 13))  # 1부터 12까지의 숫자를 원소로 가지는 리스트를 생성합니다.


def make_subset():
    n = len(A)  # 리스트 A의 길이를 구합니다.
    result = [[] for _ in range(n+1)]  # 각 원소의 개수에 따른 부분집합의 합을 저장할 리스트를 초기화합니다.
    for i in range(1 << n):  # 모든 부분집합에 대해
        sum_val = cnt_val = 0  # 부분집합의 합과 원소의 개수를 저장할 변수를 초기화합니다.
        for j in range(n):  # 각 원소에 대해
            if i & (1 << j):  # 해당 원소가 부분집합에 포함되는 경우
                sum_val += A[j]  # 부분집합의 합에 해당 원소를 더합니다.
                cnt_val += 1  # 원소의 개수를 1 증가시킵니다.
        result[cnt_val].append(sum_val)  # 원소의 개수에 따른 부분집합의 합을 저장합니다.
    return result  # 결과를 반환합니다.


for t in range(T):  # 각 테스트 케이스에 대해
    N, K = map(int, input().split())  # 원소의 개수와 부분집합의 합을 입력받습니다.
    subset = make_subset()  # 부분집합을 생성합니다.
    print(f'#{t+1} {subset[N].count(K)}')  # 원소의 개수가 N이고 합이 K인 부분집합의 개수를 출력합니다.



