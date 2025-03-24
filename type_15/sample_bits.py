'''
(ДЕЛ(405, x) → ДЕЛ(81, x)) ∨ (A – x > 162) = 1
(9x + y > A) ∨ (x ≥ 36) ∨ (y ≥ 18)
(x & A ≠ 0) → ((x & 698 = 0) → (x & 321 ≠ 0))

'''

def dell(a, b):
    return a % b == 0

for A in range(1024, 0, -1):
    flag = True
    for x in range(1025):
        F = (x & A != 0) <= ((x & 698 == 0) <= (x & 321 != 0))
        if F == 0:
            flag = False
    if flag:
        print(A)
        break
        