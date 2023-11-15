class julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f"Publication Name: {self.nimi}")


class kirja(julkaisu):
    def __init__(self, nimi, kirjailija, sivu_maara):
        super().__init__(nimi)
        self.kirjailija = kirjailija
        self.sivu_maara = sivu_maara

    def tulosta_tiedot(self):
        super().print_information()
        print(f"Author: {self.kirjailija}")
        print(f"Page Count: {self.sivu_maara}")


class lehti(julkaisu):
    def __init__(self, nimi, editoja):
        super().__init__(nimi)
        self.editoja = editoja

    def tulosta_tiedot(self):
        super().print_information()
        print(f"Chief Editor: {self.editoja}")


# Main program
aku_ankka = lehti(nimi="Aku ankka", editoja="Aki Hyyppä")
compartment_no_6 = kirja(nimi="Compartment No. 6", kirjailija="Rosa Liksom", sivu_maara=192)

# Print information for both publications
aku_ankka.tulosta_tiedot()
print("\n")
compartment_no_6.tulosta_tiedot()
