T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    # print(arr)
    result = []

    for i in range(N):  # 행방향 순회
        for j in range(N-M+1):  # 회문의 길이만큼 반복횟수 정함
            test_arr = arr[i][j:M+j]    # 테스트할 각각의 배열
            if test_arr == test_arr[::-1]:  # 회문인지 테스트
                result = ''.join(test_arr)  # 회문이라면 그 리스트를 다 붙여서 result에 담아라

    # 전치행렬 만들기
    arr_reverse = arr
    for i in range(N):
        for j in range(N):
            if i < j:
                arr_reverse[i][j], arr_reverse[j][i] = arr_reverse[j][i], arr_reverse[i][j]

    # 전치행렬에 대해서도 실행
    for i in range(N):
        for j in range(N-M+1):
            test_arr = arr_reverse[i][j:M+j]
            if test_arr == test_arr[::-1]:
                result = ''.join(test_arr)

    print(f'#{t+1} {result}')
