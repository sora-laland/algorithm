# Ai * Aj 중에서 단조증가인 것 중에서 최대
# i는 0부터 N-2번 인덱스까지 선택 가능


def check_increase(num):
    num = str(num)
    # 인접한 두 요소를 비교 -> 기준을 앞에 있는 걸로
    # num[i]과 num[i+1]
    # 여기서 i는 0부터 N-2까지 가능
    for i in range(len(num)-1):
        if num[i] > num[i+1]:
            return False
    return True


N = 4
arr = [2, 4, 7, 10]
ans = -1
for i in range(0, N-2+1):
    for j in range(i+1, N):
        print(arr[i], arr[j], arr[i]*arr[j])
        val = arr[i]*arr[j]
        # 이게 단조 증가하는 수인가?
        if check_increase(val):
            if ans < val:
                ans = val
print(ans)