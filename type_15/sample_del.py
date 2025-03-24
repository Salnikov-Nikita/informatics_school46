'''
(ДЕЛ(405, x) → ДЕЛ(81, x)) ∨ (A – x > 162) = 1
'''
def dell(a, b):
    return a % b == 0

for A in range(1, 10 ** 9):
    flag = True
    for x in range(1, 406):
        F = ((405 % x == 0) <= (81 % x == 0)) or (A - x > 162)
        if F == 0:
            flag = False
    if flag:
        print(A)
        break