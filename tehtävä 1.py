from random import randint


class Vehicle:

    def __init__(self, registeration, top_speed, current_speed=0, milage=0):
        self.registeration = registeration
        self.top_speed = top_speed
        self.current_speed = current_speed
        self.milage = milage

    def accelerate(self, change):
        self.current_speed += change
        if self.current_speed >= self.top_speed:
            self.current_speed = self.top_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def new_speed(self):
        print(f"The current speed of the car is {self.current_speed} km/h")

    def distance(self, hour):
        self.milage = (self.current_speed * hour) + self.milage

    def new_vehicle(self):
        print(f"The registeration number: {self.registeration} \n"
                f"Top speed: {self.top_speed} km/h\n"
                f"Current speed: {self.current_speed}\n"
                f"Distance: {self.milage}")


car = Vehicle("ABC-123",142,0, 0)

car.new_vehicle()

car.accelerate(30)

car.new_speed()

car.accelerate(70)

car.new_speed()

car.accelerate(50)

car.new_speed()

car.accelerate(-200)

car.new_speed()

car.new_vehicle()


cars = []
for x in range(10):
    x += 1
    rand_top_speed = randint(100, 200)
    new_car = Vehicle(f"ABC-{x}", rand_top_speed)
    cars.append(new_car)

# Race
while True:
    for car in cars:
        random_acceleration = randint(-10, 15)
        car.accelerate(random_acceleration)
        car.distance(1)

    if car.milage >= 10000:
        break

for car in cars:
    print("----------------------------------")
    car.new_vehicle()