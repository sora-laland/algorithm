# 가장 적은 시간이 걸리는 사람부터 이용해야
# 전체 대기시간을 줄일 수 있다
arr = [15, 30, 50, 10]
arr.sort()

cum_time = 0
for i in range(4):
    # print(arr)
    time = arr.pop(0)*len(arr)
    cum_time += time
print(cum_time)