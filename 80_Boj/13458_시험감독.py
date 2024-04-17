import sys; sys.stdin = open("input.txt")

N = int(input())
arr = list(map(int, input().split()))
B, C = map(int, input().split())

ans = 0
# 각 시험장을 반복
for num in arr:
    ans_1 = ans_2 = 0

    # 총감독관이 없는 경우
    if num % C == 0:
        assistant = num // C
    # 1 이상이면 한명이 더 필요함
    else:
        assistant = num // C + 1
    ans_1 += assistant



    # 총감독관이 감시하는 응시자 수 빼고 감독관의 수 +1
    if num >= B:
        num -= B
        ans_2 += 1

    # 부감독관 수 구하기
    # 나머지가 0이면, 몫 == 필요한 부감독관 수
    if num % C == 0:
        assistant = num // C
    # 1 이상이면 한명이 더 필요함
    else:
        assistant = num // C + 1
    ans_2 += assistant

    ans += min(ans_1, ans_2)


print(ans)