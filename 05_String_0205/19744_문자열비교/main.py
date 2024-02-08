# 고지식한 패턴 검색 알고리즘 사용
T = int(input())
for t in range(T):
    pattern = input()  # 찾을 문자열
    all_str = input()     # 전체 문자열
    # print(pattern)
    # print(all_str)
    i = 0
    j = 0
    while j < len(pattern) and i < len(all_str):
        if pattern[j] != all_str[i]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
    if j == len(pattern):
        result = 1
    else:
        result = 0
    print(f'#{t+1} {result}')