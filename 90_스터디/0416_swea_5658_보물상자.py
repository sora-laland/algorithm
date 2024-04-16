import sys; sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    print(f'#{t+1}', end=' ')
    N, K = map(int, input().split())
    # 문자열로 받음
    arr_str = input()

    # 총 몇 번 회전할 수 있는가?
    # 4의 배수이므로 4로 나눈 값을 사용하고 그 이후 회전은 같다
    # 또한 한 변에 위치하는 숫자도 n개이다
    n = N // 4

    # 생성 가능한 모든 수 리스트
    all_lst = []

    # 회전 생성(0번, 1번, ..., n-1번 회전)
    for x in range(n):
        # 상자의 뚜껑이 사각형이므로 한 변에 들어가는 숫자의 개수는 n개이다
        # n만큼 스텝으로 0, n, 2n, 3n...이 선택된다
        for i in range(0, len(arr_str), n):
            new_hex = arr_str[i: i + n]
            # 중복을 넣지 않으려고 not in 사용
            if new_hex not in all_lst:
                all_lst.append(new_hex)

        # 문자열 제일 뒤의 한글자를 떼서 앞으로 붙인다.
        # 대체된 문자열로 같은 로직 반복
        rotate_thing = arr_str[-1]
        arr_str = rotate_thing + arr_str[:-1]

    # 생성 가능한 모든수를 내림차순 정렬
    all_lst.sort(reverse=True)
    # 16진수를 10진수로 변환
    print(int(all_lst[K-1], 16))

