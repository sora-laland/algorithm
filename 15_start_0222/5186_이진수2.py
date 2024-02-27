import sys
sys.stdin = open("5186_input.txt", "r")
T = int(input())
for t in range(T):
    number = float(input())
    idx = []
    for n in range(1, 13):
        if number - 2 ** (-n) >= 0:
            number -= 2 ** (-n)
            idx.append(n)
            if number == 0:
                break
    # print(number)
    # print(idx)
    # 남은 값이 0이면 이진실수로 나타낼 수 있음
    # idx 리스트를 이용해서 나타내기
    result = 'overflow'
    bin = [0] * idx[-1]
    if number == 0:
        for i in idx:
            bin[i-1] = 1
        result = ''.join(map(str, bin))
    print(f'#{t+1} {result}')