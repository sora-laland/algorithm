import sys; sys.stdin = open("input.txt")

T = int(input())
for t in range(T):
    day_per, month_per, month3_per, year_per = map(int, input().split())
    day_arr = list(map(int, input().split()))

    # mon3_arr = []
    # for x in range(10):
    #     mon3_arr.append(sum(arr[x:x+3]))
    # print(mon3_arr)

    mon_arr = [0] * 12
    mon3_arr = [0] * 12


    for i in range(12):
        if day_arr[i] >= (month_per/day_per):
            mon_arr[i] = 1
            day_arr[i] = 0

    # print(day_arr)
    # print(mon_arr)


    for m in range(12):
        sum_val = 0
        for i in range(m, m+3):
            if i < 12:
                sum_val += (day_arr[i]*day_per + mon_arr[i]*month_per)
        # print(sum_val)
        if sum_val >= month3_per:
            mon3_arr[m] = 1

    for m in range(12):
        if mon3_arr[m] == 1:
            for i in range(m, m+3):
                if i < 12:
                    day_arr[i] = 0
                    mon_arr[i] = 0

    # print(day_arr)
    # print(mon_arr)
    # print(mon3_arr)

    charge = 0
    for day in day_arr:
        charge += (day * day_per)
    charge += sum(mon_arr) * month_per
    charge += (sum(mon3_arr)//3 + sum(mon3_arr)%3) * month3_per

    print(min(charge, year_per))