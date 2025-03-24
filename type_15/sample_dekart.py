'''
(9x + y > A) ∨ (x ≥ 36) ∨ (y ≥ 18)
'''

for A in range(1000, 0, -1):
    flag = True
    for x in range(1, 36):
        for y in range(1, 18):
            F = (9 * x + y > A) or (x >= 36) or (y >= 18)
            if F == 0:
                flag = False
    if flag:
        print(A)
        break
        