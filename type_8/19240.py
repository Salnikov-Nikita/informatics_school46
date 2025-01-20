alphabet = 'АВНРЬЯ'
# ЬЯРЯР
# 45353(6)
cnt = 1
out = -1
for a in alphabet:
    for b in alphabet:
        for c in alphabet:
            for d in alphabet:
                for e in alphabet:
                    word = a + b + c + d + e
                    #print(cnt, word)
                    if a != 'Я' and \
                       word.count('Ь') <= 1 and \
                       word.count('ЯЯ') == 0:
                        out = cnt
                    cnt += 1
print(out)
print(int('45353', 6) + 1)
