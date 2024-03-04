import sys; sys.stdin = open("input.txt")

for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    ans = ''
    # 겹치는 부분이 있다면
    if x1 < p2 and x2 < p1 and y1 < q2 and y2 < q1:
        ans = 'a'

    else:   # 겹치는 부분이 없다면, b c 검사
        if (x1 == p2 or y1 == q2) or (x2 == p1 or y2 == q1):
            ans = 'b'
            if (x1 == p2 and y1 == q2) or (x2 == p1 and y2 == q1):
                ans = 'c'
        else:
            ans = 'd'

    print(ans)