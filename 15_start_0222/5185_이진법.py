import sys
sys.stdin = open("5185_input.txt", "r")
T = int(input())
arr = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',
       '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']
for t in range(T):
    N, hex = input().split()
    bin = ''
    for i in hex:
        if i in 'ABCDEF':
            if i == 'A':
                T = 10
            if i == 'B':
                T = 11
            if i == 'C':
                T = 12
            if i == 'D':
                T = 13
            if i == 'E':
                T = 14
            if i == 'F':
                T = 15
            bin += arr[T]
        else:
            bin += arr[int(i)]
    print(f'#{t+1} {bin}')