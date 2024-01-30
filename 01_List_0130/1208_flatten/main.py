for tc in range(1, 11):
    dump = int(input())
    box = list(map(int, input().split()))
    for i in range(dump):
        box.sort()
        # print(sorted(box))
        box[0] += 1
        box[-1] -= 1
    max_val = max(box)
    min_val = min(box)
    print(f'#{tc} {max_val-min_val}')