'''
(x & A ≠ 0) → ((x & 698 = 0) → (x & 321 ≠ 0))
'''

for A in range(1024, 0, -1):
    flag = True
    for x in range(1025):
        F = (x & A != 0) <= ((x & 698 == 0) <= (x & 321 != 0))
        if F == 0:
            flag = False
    if flag:
        print(A)
        break
        