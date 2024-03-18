arr = [8, 1, 22, 54, 99]

# 1. 정렬된 상태의 데이터 필요
arr.sort()

# 2. 이진검색- 반복문 ver
# def binarySearch(target):
#     # 제일 왼쪽, 오른쪽 인덱스 구하기
#     low = 0
#     high = len(arr)-1
#     # 탐색 횟수
#     cnt = 0
#
#     # 해당 숫자를 찾으면 종료
#     # 더 이상 쪼갤 수 없을 때까지 반복
#     # low, high 관계가 꼬여버리면 중단
#     while low <= high:
#         mid = (low + high) // 2
#         cnt += 1
#
#         # 가운데 숫자가 정답이면 종료
#         if arr[mid] == target:
#             return mid, cnt
#         elif arr[mid] > target:  # 범위를 줄여준다
#             high = mid - 1
#         elif arr[mid] < target:
#             low = mid + 1
#     # 못찾으면 -1 반환
#     return -1, cnt


# 3. 이진 검색 - 재귀ver
def binarySearch(low, high, target):
    # 기저조건(언제까지 반복?)
    if low > high:
        return -1

    # 다음 재귀 들어가기 전엔 무엇을?
    # 정답 판별
    mid = (low + high) // 2
    if target == arr[mid]:
        return mid

    # 다음 재귀 함수 호출(파라미터)
    if target < arr[mid]:
        return binarySearch(low, mid-1, target)
    else:
        return binarySearch(mid+1, high, target)

    # 재귀 함수에서 돌아왔을 때 무엇을 해야할까?
    # 이진 검색에서는 없다

print(22, binarySearch(22))