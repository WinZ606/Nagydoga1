def szin():
    szin = str(input("Kérem a módszert: "))
    kod = str(input("Kérem a színkódot: "))
    if (szin == "HEX"):
        if (len(kod) != 6):
            print("Nem megfelelő hossz.")
        else:
            print("Megfelelő hossz.")
    elif (szin == "RGB"):
        if ((len(kod) > 11) or (len(kod) < 5)):
            print("Nem megfelelő hossz.")
        else:
            print("Megfelelő hossz.")
    elif (szin == "HSL"):
        if ((len(kod) > 13) or (len(kod) < 7)):
            print("Nem megfelelő hossz.")
        else:
            print("Megfelelő hossz.")
    else:
        print("Bonyolult kiszámolni.")