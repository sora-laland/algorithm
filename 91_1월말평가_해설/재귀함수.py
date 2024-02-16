def fibonacci(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
  
    return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))

def factorial(n):
    if n == 0:
        return 1 # 종료조건
    # 스스로를 호출하는 부분
    return n * factorial(n-1)