import sys; sys.stdin = open("input.txt")
import math



# 사칙연산 계산 함수
def calculate(a, b, operator):
    if operator == 0:
        return a + b
    elif operator == 1:
        return a - b
    elif operator == 2:
        return a * b
    elif operator == 3:
        # 소숫점 아래는 버림
        return math.trunc(a / b)


# ans = calculate(-2, 3, 3)
# print(ans)


def choice(x, ans):
    global min_val, max_val
    # 기저 조건
    # print(x, ans)
    if x == N - 1:
        # 여기서 출력되는 최대와 최소의 차이를 구해야한다
        # print(ans)
        min_val = min(min_val, ans)
        max_val = max(max_val, ans)
        return

    for idx in range(4):
        # 해당 기호를 현재 쓸 수 있다면
        if arr[idx]:
            new_ans = calculate(ans, number[x+1], idx)
            arr[idx] -= 1
            # 재귀 호출
            choice(x + 1, new_ans)
            # print(x, ans)
            arr[idx] += 1


T = int(input())
for t in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    number = list(map(int, input().split()))
    max_val = -(10 ** 8)
    min_val = (10 ** 8)

    choice(0, number[0])
    print(f'#{t+1} {max_val - min_val}')
