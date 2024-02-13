import sys
sys.stdin = open('input.txt')

# 회문 판단하기
# arr = 'abcdedcba'
# N = len(arr)
# for i in range(N//2):
#     if arr[i] != arr[N-1 - i]:
#         break
# else:
#     print('회문')
# 가장 긴 회문을 찾을 때는 가운데서 벌려 나가면서 찾음


T = 10
for t in range(10):
    N = int(input())
    arr = [input() for _ in range(8)]
    print(arr)
    # 길이가 8인 배열에서 길이가 M인 모든 연속 구간을 순회