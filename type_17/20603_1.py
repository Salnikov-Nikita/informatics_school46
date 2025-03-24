def check(subs):
    cnt = 0
    for i in subs:
        if 9_999 < i < 100_000:
            cnt += 1
    return cnt == 2

file = open('17_20603.txt')

s = [int(i) for i in file]

mx = -10 ** 9
mx = max([i for i in s if i % 10 == 5])

cnt = m_sum = 0
for i in range(len(s) - 2):
    if check(s[i:i+3]) and sum(s[i:i+3]) > mx:
        cnt += 1
        m_sum = max(m_sum, sum(s[i:i+3]))

print(cnt, m_sum)