class Pet:

    def __init__(self, name, type, tricks, health, energy, sound):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
        self.sound = sound

    def sleep(self, energy):
        energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        return self

    def noise(self):
        print(f"{self.name} says: '{self.sound}'")
        return self

    def display_info(self):
        info = self.__dict__
        print()
        print("Pet Info")
        for key in info:
            print(f"{key}: {info[key]}")
        print()
        return self