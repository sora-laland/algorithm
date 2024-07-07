import sys; sys.stdin=open('input.txt')
input = sys.stdin.readline

while True:
    password = input().rstrip()
    if password == 'end':
        break
    # is_acceptable = False

    # print(password)
    # 조건1 모음 반드시 포함
    condition_1 = False
    vowels = ['a', 'e', 'i', 'o', 'u']
    for vowel in vowels:
        if vowel in password:
            condition_1 = True
            break
    # print(condition_1)

    # 조건 2  모음 혹은 자음이 세개 연속 X
    condition_2 = False
    is_3 = ''
    for char in password:
        if char in vowels:
            is_3 += 'v'
        else:
            is_3 += 'c'
    # print(is_3)
    if ('vvv' not in is_3) and ('ccc' not in is_3):
        condition_2 = True
    # print(condition_2)

    # 조건 3 같은 글자가 연속으로 오면 안됨
    condition_3 = True
    for i in range(len(password)-1):
        if password[i] == password[i+1]:
            if password[i] not in ['e', 'o']:
                condition_3 = False
                break
    # print(condition_3)

    is_acceptable = condition_1 and condition_2 and condition_3

    if is_acceptable:
        print(f'<{password}> is acceptable.')
    else:
        print(f'<{password}> is not acceptable.')