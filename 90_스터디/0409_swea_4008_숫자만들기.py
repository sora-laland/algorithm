import sys; sys.stdin = open("input.txt")

N = int(input())
arr = list(map(int, input().split()))
number = list(map(int, input().split()))

operator = []
for i in range(4):
    for _ in range(arr[i]):
        operator.append(i)
print(operator)

path = []
used = []
def permutation(x):
    pass