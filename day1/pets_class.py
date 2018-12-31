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
        

my_pets = Pets([Dog("Tom",6),Dog("Fletcher",7),Dog("Larry",9)])
print("I have",my_pets.num_pets,"dogs.")
mammals = True
for pet in my_pets.pets_list:
    print(pet.name,"is",pet.age)
    if pet.species != "mammal":
        mammals = False
if mammals:
    print("And they're all mammals, of course.")

still_hungry = False
for pet in my_pets.pets_list:
    pet.eat()
    if pet.is_hungry:
        still_hungry = True

if still_hungry:
    print("My dogs are hungry.")
else:
    print("My dogs are not hungry.")

    

