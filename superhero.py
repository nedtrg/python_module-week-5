# Base class
class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin

    def introduce(self):
        return f"I am {self.name} from {self.origin}, and I have the power of {self.power}!"

    def use_power(self):
        return f"{self.name} uses {self.power}!"


# Inherited class
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, origin, speed):
        super().__init__(name, power, origin)
        self.speed = speed

    def fly(self):
        return f"{self.name} is flying at {self.speed} mph!"


# Testing
hero1 = Superhero("ShadowSpark", "Invisibility", "Moon City")
hero2 = FlyingSuperhero("SkyBlazer", "Flight", "Cloud Kingdom", 300)

print(hero1.introduce())
print(hero1.use_power())
print(hero2.introduce())
print(hero2.fly())
