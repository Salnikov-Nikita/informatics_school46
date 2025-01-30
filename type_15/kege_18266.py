'''
101010
011010
------
001010

x&57=0 ∨(x&23=0→¬(x&A=0))
истинна при всех натуральных значениях переменной x ?
'''
out = []
for A in range(1, 128):
    flag = True
    for x in range(1, 128):
        F = (x & 57 == 0) or ((x & 23 == 0) <= (x & A != 0)) # x&57=0 ∨(x&23=0→¬(x&A=0))
        if not F:
            flag = False
            break
    if flag:
        out.append(A)
print(out)