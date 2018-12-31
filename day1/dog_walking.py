# Parent class
class Dog:

    # Class attribute
    species = 'mammal'

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

    def eat(self):
        self.is_hungry = False

    def walk(self):
        print(self.name,"is walking")
        

# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

# Child class (inherits from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

class Pets:
    def __init__(self,pets_list):
        self.pets_list = pets_list
        self.num_pets = len(pets_list)

    def walk(self):
        for pet in self.pets_list:
            pet.walk()
        

my_pets = Pets([Dog("Tom",6),Dog("Fletcher",7),Dog("Larry",9)])
my_pets.walk()
