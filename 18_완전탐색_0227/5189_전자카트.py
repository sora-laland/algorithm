N = 3
adjl = [[0, 18, 34], [48, 0, 55], [18, 7, 0]]
path = []
result = 100 * (N-1)

def per(x): # 현재 구역을 방문한 횟수
    if x == N-1:    # 사무실 1을 제외한 나머지를 모두 방문했는지?
        print(path)
        path2 = [1] + path + [1]    # 앞뒤에 1을 끼워 넣음
        cum_sum = 0
        for p in range(len(path2)-1):
            start = path2[p] - 1  # 인접행렬 만들때 인덱스 0번이 1번이므로
            end = path2[p+1] - 1
            cum_sum += adjl[start][end]
        global result
        result = min(result, cum_sum)
        return

    for i in range(2, N+1):  # 왜 2번부터? 1번은 앞뒤로 고정이기 때문에
        if i in path: continue  # 방문을 했던 곳이면 건너뛰기
        path.append(i)
        per(x+1)
        path.pop()

per(0)
print(result)