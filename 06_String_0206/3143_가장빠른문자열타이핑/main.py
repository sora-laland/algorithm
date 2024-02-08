T = int(input())

# Brute Force
def bf(A, B):
    len_A = len(A)
    len_B = len(B)
    i = j = 0
    count = 0
    while i < len_A and j < len_B:
        if A[i] != B[j]:
            i = i - j
            j = -1  # 0 아님? -> 뒤에서 1 더해줄거라..
        i += 1
        j += 1
        if j == len_B:
            count += 1
            # 원래의 방법에선 패턴을 찾았으면 이전 시작점 다음 인덱스으로 돌아감
            # 그러나 이번엔 소거하고 이전으로 돌아가지 않는다 왜? 이제는 더이상 타자를 칠 대상이 아님
            # 단, 패턴을 탐색했던 j는 0으로 만들어 줘야함(i는 건들지마)
            j = 0
    return count


for t in range(T):
    A, B = input().split()
    result = len(A) - bf(A, B) * (len(B)-1)
    print(f'#{t+1} {result}')


# 다른 방법
#     while B in A:
#         A = A.replace(B, '_')  # B를 대신해서 _로 바꾸고 바뀐 문자열의 길이를 세면 똑같음
#         result = len(A)