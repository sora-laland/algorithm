T = int(input())
for t in range(T):
    string = input()
    result = 0
    if string[::-1] == string:
        result = 1
    print(f'#{t+1} {result}')