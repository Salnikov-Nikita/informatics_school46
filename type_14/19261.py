for x in range(37):#'0123456789abcdefghijklmnopqrstuvwxy':
    a = 9 * 37**4 + 8 * 37**3 + x * 37**2 + 3 * 37 + 1
    b = 1 * 37**4 + x * 37**3 + 9 * 37**2 + 2 * 37 + 4
    # a = int('98' + x + '31', 36) 
    # b = int('1' + x + '924', 36) 
    if (a + b) % 21 == 0:
        print((a+b) // 21, x)