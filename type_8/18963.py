alp = 'ОУКТБС'
cnt = 0
for a in alp[2:]:
    for b in alp:
        for c in alp:
            for d in alp:
                for e in alp:
                    for f in alp:
                        for g in alp:
                            for h in alp:
                                word = a + b + c +d +e +f +g +h
                                if 'КОТ' in word:
                                    cnt += 1
print(cnt)
