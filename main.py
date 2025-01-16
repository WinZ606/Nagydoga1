import szin
import oszthato
import random
import autom
from Auto import Auto

szamok = []
for i in range(0,51,1):
    szam1 = random.randint(1,100)
    szamok.append(szam1)

szin.szin()
hetes = oszthato.hettelOszthato(szamok)
print(f"A listában {hetes} darab héttel osztható szám van.")
sorok = autom.fajl()
melyik = int(input("Sorban hanyadik auto: "))
melyik -= 1
autom.kor(sorok,melyik)
autom.flotta(sorok)
autom.ertekes(sorok,melyik)
autom.kiir(sorok,melyik)
