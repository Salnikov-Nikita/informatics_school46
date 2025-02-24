a = 15625 ** 16 - 3125 ** 3 * 25 ** 19 + 625 ** 4 - 2005
cnt = 0

while a != 0:
    digit = a % 25
    if digit == 0:
        cnt += 1
    a //= 25
print(cnt)


a = ...
cnt = 0

while a != 0:
    digit = a % 49
    if digit > 9:
        cnt += 1
    a //= 49
print(cnt)