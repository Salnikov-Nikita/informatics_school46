'''
¬((¬x∨y)∧¬w)∨¬(z∧¬(y∧ w))

not((¬x∨y) and ¬w) or not(z∧¬(y∧ w))
'''
print('x y w z')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                F = not((not(x) or y) and (not w)) or not(z and not(y and w))
                if not F:
                    print(x, y, w, z)