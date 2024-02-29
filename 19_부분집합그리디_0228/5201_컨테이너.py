import sys; sys.stdin = open("5201.txt")

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    wi = list(map(int, input().split()))
    ti = list(map(int, input().split()))
    answer = 0
    wi.sort()
    ti.sort()
    # print(wi)
    # print(ti)
    # 오름차순으로 정렬해서 맨 뒤의 큰 용량부터(트럭&화물) 탐색한다
    while wi and ti:
        container = wi.pop()
        truck = ti.pop()
        if container <= truck:
            # answer += 1
            # 그 화물의 무게를 답에 더해줌
            # print(container, truck)
            answer += container
        else:
            ti.append(truck)
            # 싣을 수 없는 짐은 없애버리고 트럭은 회수
            # 트럭을 다 쓸 때까지 탐색한다
    print(f'#{t+1} {answer}')