import sys
sys.stdin = open("1240_input.txt", "r")

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    code = []
    code_key = ['0001101', '0011001', '0010011', '0111101', '0100011',
                '0110001', '0101111', '0111011', '0110111', '0001011']
    for i in range(N-1, -1, -1):
        if len(code):
            break
        for j in range(M-1, -1, -1):
            if arr[i][j] == '1':
                # print(i, j)
                code = arr[i][j-55:j+1]
                break
    check_sum = 0
    sum_val = 0
    result = 0
    # 리스트 code를 가지고 암호문 판단
    for i in range(0, 56, 7):
        a_code = code[i:i+7]
        # for n in range(10):
        #     if code_key[n] == a_code:
        #         a_code = n
        #         break
        a_code = code_key.index(a_code)
        sum_val += a_code
        if i % 2 == 0:  # 홀수자리(인덱스:짝수)
            check_sum += a_code*3
        else:
            check_sum += a_code
    if check_sum % 10 == 0:
        result = sum_val
    print(f'#{t+1} {result}')
