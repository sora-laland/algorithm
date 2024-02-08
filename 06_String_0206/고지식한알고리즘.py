def f(pat, txt, M, N):
    for i in range(0, N-M+1):  # txt에서 비교 시작 위치: N-M까지 비교 필요
        for j in range(M):  # 이 for문이 정상적으로 끝나면 검색 성공임. for-else 문법 : 다 돌았는지 확인하는데 유용
            if txt[i+j] != pat[j]:  # 불일치면 다음 시작위치로 보내기
                break
        else:                       # 매칭에 성공하면...
            return 1
    # 모든 위치에서 비교가 끝난 경우
    return 0


def bf(pattern, text):
    len_p = len(pattern)
    len_t = len(text)
    i = 0   # 전체 인덱스
    j = 0   # 패턴 탐색에 쓸 인덱스
    cnt = 0
    while i < len_t and j < len_p:
        if text[i] != pattern[i]:  # 탐색 실패의 상황
            i = i - j  # 뒤에서 1을 더해줄 것이기 때문에 i-(j+1)을 간소화
            j = -1   # 뒤에서 1을 더해주므로 0을 만들기 위해
        i += 1
        j += 1
        # 패턴을 만족시켰을 때, 즉 j가 끝까지 갔을 때(len_p-1)+1
        if j == len_p:  # 탐색 완료
            # 개별위치를 찾을 때는 인덱스를 리턴 -> i - len_p
            cnt += 1
            i = i - j + 1  # 이제 다시 찾아야 하므로 다시 초기화
            j = 0
    return cnt


# for 문으로 구현
T = int(input())
for t in range(T):
    pattern = input()
    text = input()
    M = len(pattern)
    N = len(text)
    ans = f(pattern, text, M, N)
    ans2 = bf(pattern, text)
    ans3 = text.count(pattern)  # 위 코드와 동일
    print(f'#{t+1} {ans}')

