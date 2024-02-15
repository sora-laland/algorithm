T = int(input())


# 가위바위보 함수: 이긴 사람의 인덱스를 돌려줌
def rsp(idx1, idx2):
    # idx1 < idx2 : 항상 만족하는 기본 전제조건
    # 비겼을 때 인덱스가 작은 쪽이 이기므로 idx2가 이기는 경우가 더 특별(적음)

    card1 = cards[idx1]
    card2 = cards[idx2]
    if card1 == 1 and card2 == 2:
        return idx2  # idx2가 이김
    if card1 == 2 and card2 == 3:
        return idx2  # idx2가 이김
    if card1 == 3 and card2 == 1:
        return idx2  # idx2가 이김
    return idx1


def divide(start, end):  # 구간을 나눠서 조를 만든다
    if start == end:
        return start
    mid = (start+end) // 2
    g1 = divide(start, mid)
    g2 = divide(mid+1, end)
    return rsp(g1, g2)


for t in range(T):
    N = int(input())
    cards = list(map(int, input().split()))
    answer = divide(0, N-1)
    print(answer+1)  # 왜 +1 ?? > 인덱스라서 0에서 시작하므로 i+1번째 학생의 의미로 1을 더해줌
    print(f'#{t+1} {answer+1}')
