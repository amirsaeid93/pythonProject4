class Auto:
    def __init__(self, rekisteri_numero, maksimi_nopeus):
        self.rekisteri_numero = rekisteri_numero
        self.maksimi_nopeus = maksimi_nopeus
        self.km_laskija = 0

    def ajaa(self, tunnit):
        self.km_laskija += tunnit * self.maksimi_nopeus

class Sahkoauto(Auto):
    def __init__(self, rekisteri_numero, maksimi_nopeus, akku_kapasiteetti):
        super().__init__(rekisteri_numero, maksimi_nopeus)
        self.akku_kapasiteetti = akku_kapasiteetti

class Bensaauto(Auto):
    def __init__(self, rekisteri_numero, maksimi_nopeus, tankin_tilavuus):
        super().__init__(rekisteri_numero, maksimi_nopeus)
        self.tankin_tilavuus = tankin_tilavuus

# Creating instances
sahko_auto = Sahkoauto("ABC-15", 180, 52.5)
Bensa_auto = Bensaauto("ACD-123", 165, 32.3)

# Driving cars for three hours
ajetut_tunnit = 3
sahko_auto.ajaa(ajetut_tunnit)
Bensa_auto.ajaa(ajetut_tunnit)

# Printing kilometer counters
print(f"Sähköauton kilometri laskuri näyttää: {sahko_auto.km_laskija} km")
print(f"Bensaauton kilometri laskuri näyttää: {Bensa_auto.km_laskija} km")
