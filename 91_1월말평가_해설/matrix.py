matrix = [
    [1, 2, 3], # x=0
    [4, 5, 6], # x=1
    [7, 8, 9]  # x=2
]

for x in range(len(matrix)): # 0 ~ N-1
    print(matrix[x])

for y in range(len(matrix[0])):
    for x in range(len(matrix)):
        print(matrix[x][y], end=' ')
    print()