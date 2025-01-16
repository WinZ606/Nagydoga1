class Auto:
    def __init__(self,nev,gydatum:int):
        self.nev = nev
        self.gydatum = gydatum

    def __str__(self):
        return f"Auto márkája és neve: {self.nev}\nGyártási dátuma: {self.gydatum}"