from animal import Animal
from pet import Pet
from overrides import overrides
class Cat(Animal, Pet):
    """Extends Animal AND implements the Pet interface. Inherits walk()
    from Animal as-is, overrides eat(), implements the Pet methods."""

    def __init__(self, name,legs):
        Animal.__init__(self,legs)
        self.name = name

    @overrides
    def get_name(self):
        return self.name

    @overrides
    def set_name(self, name) :
        self.name = name

    @overrides
    def play(self) :
        print(f"{self.name} is playing")

    @overrides
    def eat(self):
        print(f"{self.name} is eating")