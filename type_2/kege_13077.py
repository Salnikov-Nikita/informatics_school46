'''
¬((¬x∨y)∧¬w)∨¬(z∧¬(y∧ w))

not((¬x∨y) and ¬w) or not(z∧¬(y∧ w))
'''
print('x y w z')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                F1 = (w == x) and (y <= z)
                F2 = (w <= x) <= (y == z)
                if y == 0 and x + y + w + z <= 2 \
                    and F1 == F2 == 0:
                    print(x, y, w, z)