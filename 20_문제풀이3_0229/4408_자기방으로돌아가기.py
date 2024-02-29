import sys; sys.stdin = open("4408.txt")

T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for room in arr:
        room.sort()  # 목적지가 더 크도록 정렬
        for i in range(2):
            if room[i] % 2 == 0:  # 짝수라면 1을 빼서 홀수로 만들어줌
                room[i] -= 1
    blank = [0] * 401
    for room in arr:
        for i in range(room[0], room[1]+1):
            blank[i] += 1
    print(f'#{t+1} {max(blank)}')