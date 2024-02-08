def find_palindrome(arr, k):
    n = len(arr)
    cnt = 0
    for i in range(n):  # 행방향 탐색
        for j in range(n-k+1):
            test_str = arr[i][j:j+k]  # i번 리스트에서 [j:j+k+1]만큼의 요소 슬라이싱
            if test_str == test_str[::-1]:
                cnt += 1

    for j in range(n):  # 열방향
        for i in range(n-k+1):

            test_list = []
            for x in range(k):
                test_list.append(arr[i+x][j])    # i번째 리스트(k만큼 반복하며)에서 j번째 요소를 추출해서 새로운 리스트로 만듦

            # 위의 세줄 대신 리스트컴프리헨션 사용
            # test_list = ''.join([arr[x][j] for x in range(i, i+k)])

            # 근데 여기서 join으로 문자열 변환을 하지 않고 리스트 자체에서 회문인지 검사 가능하다
            # test_list = [arr[x][j] for x in range(i, i + k)]
            # 위와 결과는 같음

            if test_list == test_list[::-1]:  # 열을 고정하고 새로운 리스트를 만들어 회문 판별
                cnt += 1
    return cnt


T = 10
for t in range(T):
    K = int(input())
    arr = [list(input()) for _ in range(8)]
    # print(arr)
    result = find_palindrome(arr, K)
    print(f'#{t+1} {result}')