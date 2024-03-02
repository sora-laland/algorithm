import sys; sys.stdin = open("input.txt")

N = int(input())
arr = list(map(int, input().split()))
line = [0]*N
for i in range(N): # 1~N 번 학생의 최종 인덱스
    line[i] = i - arr[i]
    print(line)
    # print()
    # line.append(i-arr[i])
    for x in range(i):
        if line[x] >= line[i]:
            line[x] += 1
    print(line)
    print()

line_student = [0]*N
for n in range(N):
    line_student[line[n]] = n+1
print(*line_student)