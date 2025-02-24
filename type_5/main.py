import csv

def check(a):
    a = sorted(a)
    for i in range(len(a) - 2):
        for j in range(i + 1, len(a) - 1):
            for k in range(j + 1, len(a)):
                if a[i] * a[k] == a[j] ** 2 and a[i] != a[j]:
                    return 1
    return 0

file = open('9.7_20190.csv')

cnt = 0

for a in file:
    a = [int(i) for i in a.split(',') ]
    cnt += check(a)

print(cnt)

# a = [1, 2, 3, 4, 5]
# c = 0
# for i in range(len(a) - 2):
#         for j in range(i + 1, len(a) - 1):
#             for k in range(j + 1, len(a)):
#                  c += 1
# print(c)