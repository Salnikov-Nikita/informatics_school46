def check(s):
    for i in range(len(s) - 1):
        if int(s[i]) % 2 != 0 and int(s[i + 1]) % 2 != 0:
            return False
    return True

alp = '012345678'

num = 1
out = []
for x in alp[1:]:
    for y in alp:
        for z in alp:
            for w in alp:
                for v in alp:
                    for p in alp:
                        s = x + y + z + w + v + p
                        if num % 10 == 5 and check(s):
                            out.append([s, num])
                        num += 1

print(out[-1])