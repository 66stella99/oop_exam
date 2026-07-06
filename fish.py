from animal import Animal
from pet import Pet
from overrides import overrides
class Fish(Animal, Pet):
    def __init__(self,legs):
        Animal.__init__(self,legs)
        self.name = ""

    @overrides
    def get_name(self):
        return self.name

    @overrides
    def set_name(self, name) :
        self.name = name

    @overrides
    def play(self):
        print(f"{self.name} swims, blub blub")

    @overrides
    def walk(self):
        print(f"{self.name} can't walk, it's a fish!!")

    @overrides
    def eat(self):
        print(f"{self.name} eats")
