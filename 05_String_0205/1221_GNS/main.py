T = int(input())
for t in range(T):
    tc_num, num_str = input().split()
    # print(tc_num)
    # print(num_str)
    num = int(num_str)
    arr = input().split()
    # print(arr)
    number_str = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(num):
        for n in range(10):
            if arr[i] == number_str[n]:
                arr[i] = number[n]
    arr.sort()
    # print(arr)
    for i in range(num):
        for n in range(10):
            if arr[i] == number[n]:
                arr[i] = number_str[n]
    arr_ = ' '.join(arr)
    print(f'{tc_num} {arr_}')
