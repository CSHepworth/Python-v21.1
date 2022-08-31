from pet import Pet

class Ninja:

    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.firstname = first_name
        self.lastname = last_name
        self.pet = pet
        self.treats = treats
        self.petfood = pet_food

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        return self

    def bathe(self):
        self.pet.noise()
        return self

    def inspect_pet(self):
        self.pet.display_info()
        return self


pet1 = Pet("Fang", "Cobra", "Bite", 100, 60, "Hiss")
ninja1 = Ninja("Charles", "Norris", pet1, "Rats", "Crickets")
ninja1.walk().feed().bathe().inspect_pet()