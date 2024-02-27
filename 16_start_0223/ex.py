# 0x4A3 | 25
# print(0b11011110 & 0b11011)
# print(0x4A3|25)

def code(a):
    return a ^ KEY


KEY = 1004
# print(code(1000))
# print(code(4))

# num = 0b1
# for i in range(5):
#     print(bin(num), num)
#     num = num << 1


# N = 5
# M = 31
# bin_num = str(bin(M))
# print(bin_num)
# msg = 'ON'
# for i in range(N):
#     if bin_num[N+1-i] == '0':
#         msg = 'OFF'
# print(msg)

# 다른 방법
# 1111 에 1을 더해주면 자리수가 올라가면서 10000이 되는 것 이용

# 강사님 풀이
# M = 32
# N = 5
# def test():
#     tar = M
#     for i in range(N):
#         if tar & 0x1 == 0:
#             return False
#         tar = tar >> 1
#     return True
# print(test())
#
# t1 = 1
# print(f'{t1}')
# print(f'{t1:.50f}')

print('1DB176C588D26EC')
print(len('1DB176C588D26EC'))
print()

print(bin(int('1DB176C588D26EC', 16)))
print(bin(0x1DB176C588D26EC >> 2))
print(len(bin(0x1DB176C588D26EC)))
print(len('1110110110001011101101100010110001000110100100110111011'))
#01110110110001011101101100010110001000110100100110111011