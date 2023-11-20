class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f"Julkaisun nimi on: {self.nimi}")


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjailija, sivu_maara):
        super().__init__(nimi)
        self.kirjailija = kirjailija
        self.sivu_maara = sivu_maara

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Kirjailijan nimi on: {self.kirjailija}")
        print(f"Kirjan sivu määrä on: {self.sivu_maara}")


class Lehti(Julkaisu):
    def __init__(self, nimi, toimittaja):
        super().__init__(nimi)
        self.toimittaja = toimittaja

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Päätoimittaja on: {self.toimittaja}")


# Main program
aku_ankka = Lehti(nimi="Aku ankka", toimittaja="Aki Hyyppä")
hytti_numero_6 = Kirja(nimi="Hytti numero 6", kirjailija="Rosa Liksom", sivu_maara=192)

# Print information for both publications
aku_ankka.tulosta_tiedot()
print("\n")
hytti_numero_6.tulosta_tiedot()
