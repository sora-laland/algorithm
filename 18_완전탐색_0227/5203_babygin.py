import sys; sys.stdin = open("5203.txt")

T = int(input())
for t in range(T):
    arr = list(map(int, input().split()))
    player1 = arr[0:3:2]
    player2 = arr[1:4:2]
    win = 0
    winner = 0

    def is_baby_gin(card):
        global win
        tri = run = 0
        if card[0] == card[1] == card[2]:
            tri = 1
        if card[0]+2 == card[1]+1 == card[2]:
            run = 1
        if tri or run:
            win = 1
            return True
        else:
            return False


    path = []
    used = [False for _ in range(6)]

    def perm(n, card):
        if n == 3:
            # print(path)
            is_baby_gin(path)
            return
        for i in range(len(card)):
            if used[i]:
                continue
            used[i] = True
            path.append(card[i])
            perm(n + 1, card)
            path.pop()
            used[i] = False

    for i in range(4, 12):
        if i % 2 == 0:
            player1.append(arr[i])
            # print(player1, player2)
            perm(0, player1)
            if win == 1:
                winner = 1
                break
        else:
            player2.append(arr[i])
            # print(player1, player2)
            perm(0, player2)
            if win == 1:
                winner = 2
                break
        # 여기서 주어진 카드들로 모든 중복 순열을 만들고 베이비진 판별
    print(f'#{t+1} {winner}')