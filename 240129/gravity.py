'''
9
7 4 2 0 0 6 0 7 0
9
7 8 2 0 0 6 0 7 0
'''
N = int(input())    # 상자가 쌓여있는 가로 길이
arr = list(map(int, input().split('')))

max_v = 0   # 가장 큰 낙차
for i in range(N-1):
    cnt = 0     # 오른쪽에 있는 더 낮은 높이 의 초기값
    for j in range(i+1, N):
        if arr[i]>arr[j]:
            cnt +=1
    if max_v < cnt:     # 최대 낙차보다 크면
        max_v = cnt
print(max_v)