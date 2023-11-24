class Animal:

    def __init__(self, type, sound):
        self.type = type
        self.sound = sound

    def make_sound(self):
        print(f'{self.type}, {self.sound}')

 class Bird(Animal):

        def __init__(self, type, sound, color):
            super().__init__(type, sound)
            self.color = color

animal1 = Animal("Lion", "Roar")
animal2 = Animal("Tiger", "Growl")
animal3 = Animal("bird", "kukkuu")
animal1.make_sound()
animal2.make_sound()


class Zoo:
    def __int__(self):
        self.animals = []


    def add_animal(self, animal):
        self.animals.append(Animal)
        return

    def list_animal(self, animals)



happy_animals = Zoo()
happy_animals.animals.append(animal1)
happy_animals.animals.append(animal2)



