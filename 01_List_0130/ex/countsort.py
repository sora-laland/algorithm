N = 6
K = 9
data = [7, 2, 4, 5, 2, 3]
counts = [0] * (K+1)
temp = [0] * N
# 배열에 기록하기
for x in data:
    counts[x] += 1
# print(counts)

for i in range(1, K+1):
    counts[i] = counts[i-1] + counts[i]
# print(counts)

for i in range(N-1, -1, -1):     # N-1부터 0까지 역순으로
    counts[data[i]] -= 1    # 개수를 인덱스로 변환(남은개수)
    temp[counts[data[i]]] = data[i]
    # print(counts)
print(temp)