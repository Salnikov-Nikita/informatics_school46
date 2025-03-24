'''
¬(x→y)∨(z→w)∨¬z
x y x→y x<=y not(x) or y
0 0  1   1      1
0 1  1   1      1
1 0  0   0      0
1 1  1   1      1
'''
print('x y z w')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                F = not(x <= y) or (z <= w) or (not(z))
                if F == 0: # not F 
                    print(x, y, z, w)