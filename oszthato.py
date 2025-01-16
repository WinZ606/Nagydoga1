def hettelOszthato(szamok):
    hanyvan = 0
    for i in range(0,len(szamok),1):
        if (szamok[i] % 7 == 0):
            hanyvan += 1
    return hanyvan