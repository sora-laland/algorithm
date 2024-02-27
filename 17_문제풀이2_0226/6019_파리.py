import sys
sys.stdin = open("6019.txt")

T = int(input())
for t in range(T):
    D, A, B, F = map(int, input().split())
    ans = F * D / (A+B)
    print(f'#{t+1} {ans}')
