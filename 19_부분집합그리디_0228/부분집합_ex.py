arr = ['A', 'B', 'C', 'D', 'E']
n = len(arr)


def get_sub(tar):
    cnt = 0
    for i in range(n):
        # 1비트가 1인지 확인
        if tar & 0x1:   # 가독성 때문에 16진수로 써줌(비트연산임을 나타냄)
            cnt += 1
            # print(arr[i], end=' ')
        # 오른쪽 끝 비트를 하나씩 제거
        tar >>= 1
    return cnt


result = 0
for tar in range(1 << n):  # 2의 n제곱 만큼
    if get_sub(tar) >= 2:
        result += 1
print(result)