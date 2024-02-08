def f(i, k):  # i 현재위치, k 목표
    if i == k:
        return
    else:
        print(arr[i])
        f(i+1, k)


arr = [10, 20, 30]
N = len(arr)
f(0, N)