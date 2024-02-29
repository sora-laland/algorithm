# 주사위
N = 3
path = []
# 중복순열에서 start를 추가하자

def func(lev, start):
    if lev == N:
        print(path)
        return

    for i in range(start, 7):
        path.append(i)
        func(lev+1, i)
        # 여기서 시작점이 i인 이유 : 이전 선택 값으로 진입 가능하다
        # 1, 1, 1 이라고 해서 같은 1이 아니라 서로 다른 주사위위        path.pop()

func(0, 1)