arr = ['A', 'B', 'C', 'D', 'E']
#  총 10가지
# A B C
# A B D
# A B E
# A C D
# A C E
# A D E
# B C D
# B C E
# B D E
# C D E
path = []
n = 3


def run(lev, start):
    if lev == n:
        print(path)
        return

    for i in range(start, len(arr)):
        path.append(arr[i])
        run(lev+1, i+1)
        path.pop()


run(0, 0)


