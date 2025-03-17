s = '0123456789abcde'
for A in range(1, 10 ** 6):
    for x in s:
        num_1 = int('432' + x + '3', 15)
        num_2 = int('86' + x + '86', 15)
        if (num_1 + A) % num_2 == 0:
            print(A)
            break
