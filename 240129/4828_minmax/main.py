# 테스트케이스를 T를 받는다
T = int(input())  # 테스트케이스의 숫자 T
# print(T)  # 3을 출력
for t in range(T):  # T번 반복해서 테스트케이스 별 입력받기
    N = int(input())    # N개의 입력
    a = list(map(int, input().split()))   # 각각의 요소(=문자열)을 정수로 변환
    # print('a', a)  # 주석처리 필
    max_val = max(a)
    min_val = min(a)
    print(f'#{t+1} {max_val - min_val}')