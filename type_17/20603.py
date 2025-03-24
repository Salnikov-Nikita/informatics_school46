def check(a, b, c):
    cnt = 0
    if 9_999 < a < 100_000:
        cnt += 1
    if 9_999 < b < 100_000:
        cnt += 1
    if 9_999 < c < 100_000:
        cnt += 1
    return cnt == 2

file = open('17_20603.txt')

s = [int(i) for i in file]

mx = -10 ** 9
mx = max([i for i in s if i % 10 == 5])

# for i in s:
#     if i % 10 == 5:
#         mx = max(mx, i)

cnt = m_sum = 0
for i in range(len(s) - 2):
    a = s[i]
    b = s[i + 1]
    c = s[i + 2]
    if check(a, b, c) and a + b + c > mx:
        cnt += 1
        m_sum = max(m_sum, a + b + c)

print(cnt, m_sum)