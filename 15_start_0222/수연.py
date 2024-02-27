import sys
sys.stdin = open("1240_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(N)]
    # print(arr)

    for i in range(N):
        if 1 in arr[i]:
            line_reverse = arr[i][::-1]
            break
    print(line_reverse)

    for j in range(M):
        if line_reverse[j] == 1:
            code = line_reverse[j:j+56]
            code.reverse()
            break
    print(code)
    print(len(code))


    print(f'#{tc} {N} {M} code: {code}')