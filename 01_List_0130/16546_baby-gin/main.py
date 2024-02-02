T = int(input())
for t in range(T):
    num = int(input())
    c = [0] * 12  # 뒤에서 코드를 줄이기 위해 더미

    for _ in range(6):
        c[num % 10] += 1
        num //= 10
    # print(c)
    i = 0   # 검사할 인덱스 초기값, 뒤에서 조사가 끝나면 1 올려줌
    tri = run_ = 0  # swea는 'run'을 거부하므로 쓰지 않는다
    while i < 10:
        if c[i] >= 3:  # 트리플렛 조사 후 데이터삭제
            c[i] -= 3
            tri += 1
            continue  # 같은 자리에서 한번 더 조사 필요
        if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1:  # 연속된 인덱스에 값이 있을 때 run
            c[i] -= 1
            c[i+1] -= 1
            c[i+2] -= 1
            run_ += 1
            continue    # 같은 자리에서 한번 더 조사 필요
        i += 1

    if run_ + tri == 2:
        result = 'true'
    else:
        result = 'false'

    print(f'#{t+1} {result}')
