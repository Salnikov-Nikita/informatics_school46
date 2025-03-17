# alph = '0123456789ABCDEFGH'
# for y in alph:
#     s = 'A2B83' + y + '7'
#     if int(s, 18) % 5 == 0:
#         print(y, s, int(s, 18))

alph = '0123456789A'
m = -1
for y in alph:
    for x in alph:
        s1 = '65897' + x + '21'
        s2 = '2' + y + '923'
        if (int(s1, 11) + int(s2, 11)) % 31 == 0:
            m = max(m, int(x, 11))
print(m)