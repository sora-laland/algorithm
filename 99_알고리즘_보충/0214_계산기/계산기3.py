# 후위표기법으로..
# 연산자는 무조건 push하는데 이때 우선순위를 잘 봐서 결정
# 연산자/피연산자를 구분

N = int(input())
infix = input()
postfix = ''
S = []
icp = []
for tk in infix:
    if tk in icp:
        if tk == '(': # 여는 괄호 부분은 빼도 됨
            pass
        elif tk == ')':
            pass
        else:
            pass
    else:
        pass

# 남아있는 연산자들 출력 -> 스택은 비어있음

# 후위를 이용해 다시 계산할 차례
for tk in postfix:
    if tk in icp:
        a = S.pop()
        b = S.pop()
        # if tk == '*':