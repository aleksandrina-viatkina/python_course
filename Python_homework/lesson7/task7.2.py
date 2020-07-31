from abc import ABC, abstractmethod

class Textile(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def textile_extense(self):
        pass

class Coat(Textile):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    @property
    def textile_extense(self):
        return f'Расход ткани на пальто составит: {self.size/ 6.5 + 0.5:.2f}'

class Suit(Textile):
    def __init__(self, name, growth):
        self.name = name
        self.growth = growth

    @property
    def textile_extense(self):
        return f'Расход ткани на костюм составит: {2 * self.growth + 0.3:.2f}'

coat = Coat('FINN FLARE',200)
suit = Suit('Henderson', 300)
print(coat.textile_extense)
print(suit.textile_extense)
