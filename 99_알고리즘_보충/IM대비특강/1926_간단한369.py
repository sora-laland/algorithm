import sys
sys.stdin = open("1926.txt")

# 369의 개수만큼 -를 출력
def count_369(num):
    # 문자열이 아닌 정수로 처리 -> 10으로 나눠서 나머지를 보기
    cnt = 0
    while num > 0:
        val = num % 10
        if val == 3 or val == 6 or val == 9:
            cnt += 1
        num //= 10
    return cnt

# 이렇게 해도 되고
# for num in range(1, 50):
# #     num = str(num)
# #     cnt = 0
# #     for val in num:
# #         # 3이나 6이나 9면 -를 출력
# #         if val in '369':
# #             cnt += 1

# 함수 호출도 가능
N = int(input())
for num in range(1, N+1):
    cnt = count_369(num)
    if cnt == 0:
        print(num, end=' ')
    else:
        print('-' * cnt, end=' ')


# 함수로 만들어볼까요?
