class Superhero:
    def __init__(self, name, powers, weaknesses):
        self.name = name
        self.powers = powers
        self.weaknesses = weaknesses

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Powers: {self.powers}")
        print(f"Weaknesses: {self.weaknesses}")

    def use_power(self, power):
        if power in self.powers:
            print(f"{self.name} is using {power}")
        else:
            print(f"{self.name} does not have the power {power}")

    def show_weaknesses(self):
        print(f"Weaknesses: {self.weaknesses}")

class Villain(Superhero):
    def __init__(self, name, powers, weaknesses, evil_plan):
        super().__init__(name, powers, weaknesses)
        self.evil_plan = evil_plan

    def display_info(self):
        super().display_info()
        print(f"Evil Plan: {self.evil_plan}")

    def execute_plan(self):
        print(f"{self.name} is executing their evil plan")

superhero1 = Superhero("Iron Man", ["Flight", "Super Strength"], ["Kryptonite", "Explosions"])
villain1 = Villain("Thanos", ["Telekinesis", "Mind Control"], ["Infinity Gauntlet", "Avengers"], "Destroy the Universe")

class Car:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

    def move(self):
        print(f"{self.color} {self.make} {self.model} is driving")

class Plane:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

    def move(self):
        print(f"{self.color} {self.make} {self.model} is flying")

car1 = Car("Toyota", "Camry", "blue")
plane1 = Plane("Boeing", "747", "silver")

car1.move()
plane1.move()