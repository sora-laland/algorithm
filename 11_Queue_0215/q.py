N = 10      # 큐 생성
q = [0] * 10
front = rear = -1       # 초기화

rear += 1       # enQueue(10)
q[rear] = 10
rear += 1       # enQueue(20)
q[rear] = 20
rear += 1       # enQueue(30)
q[rear] = 30

while front != rear:    # 큐가 비어있지 않으면
    front += 1      # deQueue()
    print(q[front])

# 특정 인덱스에 접근해서 데이터를 가져오기만 하기때문에 속도 빠름
# append, pop은 느림
# 연산을 함수로 구현은 알아서 해보기
