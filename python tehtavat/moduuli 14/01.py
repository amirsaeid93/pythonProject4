class Tili:

    def __init__(self, omistajan_nimi, rahan_maara = 0):
        self.omistajan_nimi = omistajan_nimi
        self.rahan_maara = rahan_maara

    def maksa(self, summa):
        if self.rahan_maara - summa < 0:
            print(f'Sinulla ei ole tarpeeksi rahaa tililläsi {self.omistajan_nimi}, jotta voisit maksaa valitsemasi summan.')
        else:
            self.rahan_maara - summa
            self.rahan_maara = self.rahan_maara - summa
            print(f'Sinulla on enään {self.rahan_maara} Euron verran rahaa jäljellä tililläsi {self.omistajan_nimi}.')

    def tulostus(self):
        print(f'Tilin omistajan nimi on {self.omistajan_nimi} ja tilillä olevan rahan määrä on {self.rahan_maara}.')

print("--- tilien luonti ---")
t1 = Tili("Jorma")
t2 = Tili("Anne", 100)
print("--- maksut ---")
t1.maksa(25)
t2.maksa(25)
print("--- tilien saldot ---")
t1.tulostus()
t2.tulostus()