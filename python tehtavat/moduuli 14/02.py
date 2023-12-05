class Person:

    def __init__(self, etunimi, sukunimi):
        self.etunimi = etunimi
        self.sukunimi = sukunimi

    def plot(self):
        print(f'Hei olen {self.etunimi} {self.sukunimi}')


class Student(Person):
    def __init__(self, etunimi, sukunimi, opiskelija_numero):
        self.opiskelija_numero = opiskelija_numero
        super().__init__(etunimi, sukunimi)

    def plot(self):
        print(f'Hei olen {self.etunimi} {self.sukunimi} ja opiskelija numeroni on {self.opiskelija_numero}')



p1 = Person("James", "Bond")
s1 = Student("Johnny", "English", 321)
p1.plot()
s1.plot()

