import sys
sys.stdin = open('1242.txt')

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    # print(arr)
    check = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] != '0':
                codes = arr[i][j:j+15]  # 길이는 고정이 아니라 유동적
                if codes not in check:
                    check.append(codes)
                break   # 다음 행에서는 확인
    # print(check)

    bin_codes = []
    for code in check:
        bin_codes.append(bin(int(code, 16)))
    # print(bin_codes)

    trim_bin_codes = []
    for code in bin_codes:
        for i in range(len(code)-1, -1, -1):
            if code[i] == '1':
                trim = code[2:i+1]
                trim = '0'*(57-i) + trim    # 앞에 0 넣어주기
                trim_bin_codes.append(trim)
                break
    # print(trim_bin_codes)
    # print(len(trim_bin_code[0]), len(trim_bin_code[1]))

    code_key = ['0001101', '0011001', '0010011', '0111101', '0100011',
                '0110001', '0101111', '0111011', '0110111', '0001011']
    # 이진수로 변환했으니 키 값과 비교해서 숫자로 바꾸면서 조건 확인
    sum_val = 0
    for code in trim_bin_codes:
        check_sum = 0
        all_sum = 0
        for i in range(0, 56, 7):
            a_code = code[i:1+7]
            if a_code in code_key:
                code_key.index(code[i:i+7])
            if i % 2 == 1:  # 짝수라면
                check_sum += a_code
                all_sum += a_code
            else:
                check_sum += 3*a_code
                all_sum += a_code
        if check_sum % 10 == 0:
            sum_val += all_sum
    print(f'{t+1} {sum_val}')