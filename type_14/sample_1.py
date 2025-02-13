alp = '0123456789ABCDEFGH'

# for i in range(65, 100):
#     print(chr(i), end='')

for x in alp:
    # print(x, end=' ')
    a = int('11H' + x + '05', 18)
    b = int('3F' + x + '54' + x +'8', 18)
    c = int('G' + x + x + x + '9' , 18)
    if (a + b + c) % 14 == 0:
        print(x, (a + b + c) // 14)

# print('9600497')