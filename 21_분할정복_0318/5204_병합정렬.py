import sys; sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0

    def merge_sort(unsorted_list):
        global cnt

        if len(unsorted_list) == 1:
            return unsorted_list

        mid = len(unsorted_list) // 2
        left = unsorted_list[:mid]
        right = unsorted_list[mid:]

        left = merge_sort(left)
        right = merge_sort(right)

        if left[-1] > right[-1]:
            cnt += 1

        return merge(left, right)


    def merge(left, right):
        i = j = 0
        result = []

        while len(left) > i or len(right) > j:
            # 둘 다 요소가 남아있다면
            if len(left) > i and len(right) > j:
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            elif len(left) > i:
                result.append(left[i])
                i += 1
            elif len(right) > j:
                result.append(right[j])
                j += 1
        return result

    answer = merge_sort(arr)
    print(f'#{t+1} {answer[N//2]} {cnt}')