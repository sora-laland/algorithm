import sys; sys.stdin = open("input.txt")
N, K = map(int, input().split())
grade = [0] * 12
room = 0
for _ in range(N):
    S, Y = map(int, input().split())
    grade[S + 2 * (Y-1)] += 1   # 해당되는 배열에 카운트

for i in grade:
    room += i//K
    if i % K:
        room += 1
print(room)