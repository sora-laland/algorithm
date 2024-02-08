T = int(input())
for t in range(T):
    str1 = list(input())
    str2 = list(input())
    print(str1)
    print(str2)

    # 카운트를 이용
    cnt = [0] * len(str1)
    # print(cnt)

    # 해당 문자가 있으면 같은 위치의 cnt 배열 카운트를 올림
    # for item in str2:
    #     for idx in range(len(str1)):
    #         if item == str1[idx]:
    #             cnt[idx] += 1
    for i in str2:
        if i in str1:
            cnt[str1.index(i)] += 1  # 이렇게만 하면 i가 str1에 없을 때 문제! if를 넣어줘야 한다
            # .index()메서드는 가장 왼쪽 인덱스를 반환하기 때문에 중복을 제거하는 효과
    print(cnt)

    print(f'#{t+1} {max(cnt)}')