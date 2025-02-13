a = 15625 ** 16 - 3125 ** 3 * 25 ** 19 + 625 ** 4 - 2005
# A - 65; a - 97

s = ''
while a != 0:
    digit = a % 25
    if digit > 9:
        s = chr(digit + 87) + s
    else:
        s = str(digit) + s
    a //= 25

print(s, s.count('0'))