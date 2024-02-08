T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    print(arr)
    result = []
    for i in range(N):  # 행방향 순회
        for j in range(N-M+1):  # 회문의 길이만큼 반복횟수 정함
            test_arr = arr[i][j:M+j]    # 테스트할 각각의 배열
            if test_arr == test_arr[::-1]:  # 회문인지 테스트
                result = ''.join(test_arr)  # 회문이라면 그 리스트를 다 붙이고 result 에 담아라

    for i in range(N):  # 열방향 순회
        for k in range(N-M+1):  # 회문의 길이만큼 반복횟수 정함
            test_col_arr = []   # 테스트할 각각의 배열을 담을 준비
            for j in range(k, k+M):
                test_col_arr.append(arr[j][i])  # i는 고정 시키고 j를 k~k+M 구간에서 뽑아 리스트로 만들기
            if test_col_arr == test_col_arr[::-1]:  # 회문인지 테스트
                result = ''.join(test_col_arr)

    arr_reverse = arr
    for i in range(N):
        for j in range(N):
            if i < j:
                arr_reverse[i][j], arr_reverse[j][i] = arr_reverse[j][i], arr_reverse[i][j]
    print(arr_reverse)


    print(f'#{t+1} {result}')
