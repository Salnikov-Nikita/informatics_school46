# for i in range(65, 100):
#     print(chr(i), end='')

# alph = '0123456789ABCDEFGH'
# for y in alph:
#     s = 'A2B83' + y +'7'
#     if int(s, 18) % 5 == 0:
#         print(y, s, int(s, 18))


out = []
for x in range(37):
    for y in range(37):
        a = 7 + y * 37 + 3 * 37**2 +8 * 37**3 + 6 * 37**4 +\
        6 * 37**5 + x * 37**6 + 2 * 37**7 + 10 * 37**8
        if a % 32 == 0:
            out.append(x + y * 37)
print(max(out), out)



# alph = '0123456789A'
# for y in alph:
#     for x in alph:
#         s_1 = '65897' + x +'21'
#         s_2 = '2' + y + '923'
#         if (int(s_1, 11) + int(s_2, 11)) % 31 == 0:
#             print(x, (int(s_1, 11) + int(s_2, 11)) // 31)
