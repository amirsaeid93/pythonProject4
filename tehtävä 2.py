class Hissi:

    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.kerros = 0

    def siirry_kerrokseen(self, mihin):
        if mihin > self.ylin_kerros:
            print(f'Ei voida siirtyä {mihin} kerrokseen. Rakennuksen ylin kerros on {self.ylin_kerros}.')
        elif mihin < self.kerros:
            for _ in range(self.kerros-mihin):
                self.kerros_alas()
        else:
            for _ in range(mihin-self.kerros):
                self.kerros_ylös()
    def kerros_ylös(self):
        self.kerros += 1
        print(f'Olet kerroksessa {self.kerros}')

    def kerros_alas(self):
        self.kerros -= 1
        print(f'Olet kerroksessa {self.kerros}')



class Talo:

    def __init__(self, alin_kerros, ylin_kerros, hissien_lukumäärä):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissien_lukumäärä = hissien_lukumäärä
        self.hissit = []

        for _ in range(self.hissien_lukumäärä):
            hissi = Hissi(self.alin_kerros, self.ylin_kerros)
            self.hissit.append(hissi)

    def aja_hissiä(self, hissin_numero, kohde_kerros):
        self.hissit[hissin_numero].siirry_kerrokseen(kohde_kerros)


h = Hissi(0, 5)

h.siirry_kerrokseen(4)
h.siirry_kerrokseen(1)
h.siirry_kerrokseen(5)

talo = Talo(0, 5, 3)
talo.aja_hissiä(0, 3)
talo.aja_hissiä(1, 5)
talo.aja_hissiä(2, 2)

