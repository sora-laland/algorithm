# 고지식한 알고리즘 패턴 매칭
T = 10
for t in range(T):
    tc = int(input())
    pattern = input()
    text = input()

    M = len(pattern)
    N = len(text)
    cnt = 0

    # 수업시간에 알려주신 for-else 문법 사용
    # for i in range(0, N-M+1):  # txt에서 비교 시작 위치: N-M까지 비교 필요
    #     for j in range(M):  # 이 for문이 정상적으로 끝나면 검색 성공
    #         if text[i + j] != pattern[j]:  # 불일치면 다음 시작위치로 보내기
    #             break
    #     else:  # 매칭에 성공하면...
    #         cnt += 1


    # while 문으로 풀어보기
    i = 0   # 전체의 인덱스
    j = 0   # 패턴의 인덱스
    while j < M and i < N:
        if pattern[j] != text[i]:
            i = i - j
            j = -1
        i += 1
        j += 1
        if j == M:
            cnt += 1    # 일치하는 것을 찾으면 카운트 올리고
            i = i - j + 1   # 이제 그 위치의 다음 인덱스 부터 다시 찾기 시작(1을 여기선 더해줘야함)
            j = 0

    print(f'#{t+1} {cnt}')
