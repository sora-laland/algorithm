'''
3
1 2 3
4 5 6
7 8 9
'''

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr2 = [[0]*N for _ in range(N)]
arr3 = [[0]*N]*N  # 이런거 하지마라
print(arr3)
arr[0][0] = 1
print(arr3)
