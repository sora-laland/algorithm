import sys; sys.stdin = open("input.txt")

N = int(input())
for n in range(N):
    Na, *A = map(int, input().split())
    Nb, *B = map(int, input().split())

    cnt_a = [0] * 4
    cnt_b = [0] * 4

    for a in A:
        cnt_a[a-1] += 1
    cnt_a.reverse()

    for b in B:
        cnt_b[b-1] += 1
    cnt_b.reverse()

    winner = "D"
    for i in range(4):
        if cnt_a[i] > cnt_b[i]:
            winner = "A"
            break
        elif cnt_b[i] > cnt_a[i]:
            winner = "B"
            break
        else:
            continue

    # print(cnt_a)
    # print(cnt_b)
    print(winner)
    # print()
