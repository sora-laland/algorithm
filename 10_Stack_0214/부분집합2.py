'''
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}의 powerset 중
원소의 합이 10인 부분집합을 구하시오 by 백트랙킹
'''
# bit[i]에서 원소 포함여부를 0, 1로 표현
# 지금 방법보다 후보를 고를 때마다 합을 구하면서
# 타겟을 넘으면 그 부분은 버리는 방식이 더 효율적
# i-1까지의 합 : S
# 뒤에 i번째 원소를 포함할꺼면 S+A[i]


def f(i, k, s, t): # k개의 원소를 가진 배열A, 부분집합 합이 t인 경우
    global cnt
    cnt += 1
    if s == t:  # 모든 원소에 대해 결정하면(부분집합이 완성되는 부분)
        for j in range(k):
            if bit[j]:  # A[i]가 포함된 경우
                print(A[j], end=' ')
        print()
    elif i == k:
        return
    elif s > t: # 고려한 원소의 합이 t보다 큰 경우
        return
    else:
        for j in range(1, -1, -1):
            bit[i] = j
            f(i+1, k, s+A[i]*j, t)
        # bit[i] = 1    # 위 for문과 동일
        # f(i+1, k, s+A[i], t)
        # bit[i] = 0
        # f(i+1, k, s, t)

N = 10
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0] * N
cnt = 0
f(0, N, 0, 50)
print(f'cnt:', cnt)