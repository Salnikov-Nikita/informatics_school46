a = 4 * 3125**2019 + 3 * 625**2020 - 2 * 125**2021 \
    + 25**2022 - 4 * 5**2023 - 2024

# s = '123ABCDF'
# for c in s:
#     if c.isdigit():
#         print(c)  

#1
s = ''
while a != 0:
    if a % 25 > 10:
        s = chr(55 + a % 25) + s
    a //= 25
print(s)
print(len(s))

#2
# s = ''
# while a != 0:
#     if a % 25 > 9:
#         s = chr(55 + a % 25) + s
#     else:
#         s = str(a % 25) + s
#     a //= 25

# alp = '0123456789A'
# for c in alp:
#     s = s.replace(c, '')
# print(len(s))

#3
# cnt = 0
# while a != 0:
#     if a % 25 > 10:
#         cnt += 1
#     a //= 25
# print(cnt)