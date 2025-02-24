def f(n, o):
    s = ''
    if n == 0:
        return '0'
    while n != 0:
        s = str(n % o) + s
        n //= o
    return s

# 0123456789
# 1010101111
# 1010101 1 1 1
#        -3-2-1
for i in range(1_000_000):
    s = bin(i)[2:]
    if i % 2 == 0:
        s += s[-2] + s[-1]
    else:
        s += '011'
    if int(s, 2) > 300:
        print(i)
        break
    # print(i, bin(i)[2:], f(i, 2), f(i, 4), f(i, 5))

a = 38
print(a, bin(a)[2:], bin(a)[2:] + '100', int(bin(a)[2:] + '100', 2) )