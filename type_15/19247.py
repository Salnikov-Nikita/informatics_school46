for A in range(1, 1000):
    flag = True
    for x in range(1, 57):
        for y in range(1, 401):
            F = (x - 3 * y < A) or (y > 400) or (x > 56)
            if not F:
                flag = False
    if flag:
        print(A)
        break