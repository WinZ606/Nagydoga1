from Auto import Auto

def fajl():
    autolista = []

    f = open("auto.txt", "r", encoding="utf-8")
    f.readline().strip()
    sorok = f.readlines()
    f.close()
    
    i = 0
    
    while i < len(sorok):
        adatok = sorok[i].strip().split(":")
        nev, gydatum = adatok
        auto = Auto(
            nev.strip(),
            int(gydatum.strip())
        )
        autolista.append(auto)
        i += 1

    return autolista

def kor(sorok,melyik):
    print(f"{sorok[melyik].nev} - {2025 - sorok[melyik].gydatum} éves")

def flotta(sorok):
    print(f"Autók száma: {len(sorok)}.")

def ertekes(sorok,melyik):
    neve = sorok[melyik].nev
    datum = sorok[melyik].gydatum
    print(f"A legöregebb autó: {neve}, {datum}")

def kiir(sorok,melyik):
    f = open("ki.txt", "a")
    f.write(f"{sorok[melyik].nev} - {2025 - sorok[melyik].gydatum} éves")