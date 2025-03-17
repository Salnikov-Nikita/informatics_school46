'''
943697x21 – 2y9253
'''

out_diff = []
out_nums = []
alp = '0123456789ABCDEFGHIJK'
for x in alp:
    for y in alp:
        a = int('943697' + x + '21', 21)
        b = int('2' + y + '9253', 21)
        if (a - b) % 20 == 0:
            out_diff.append(int(x, 21) - int(y, 21))
            out_nums.append((a - b) // 20)
print(out_nums[out_diff.index(max(out_diff))])
print(max(out_diff))

a = int('943697K21', 21)
b = int('209253', 21)
print((a - b) // 20)
# for i in range(192):
#     print(chr(i), end='')