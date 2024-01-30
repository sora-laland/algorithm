T = int(input())
for t in range(T):
    N = int(input())
    lst = []
    for n in range(N):
        Ai, Bi = map(int, input().split())
        # print(T, N, Ai, Bi)
        lst.append(list(range(Ai, Bi+1)))
    print(lst)

    P = int(input())
    count = [0] * P
    print(count)
    Cj_lst = []
    for p in range(P):
        Cj = int(input())
        Cj_lst.append(Cj)

    for i in range(P):
        for j in range(N):
            if Cj_lst[i] in lst[j]:
                count[i] += 1
    print(count)
    print(list(map(str, count)))