from abc import ABC, abstractmethod


class Clothing(ABC):
    @abstractmethod
    def fabric_amount(self):
        pass


class Coat(Clothing):
    def __init__(self, v):
        self.v = v

    @property
    def fabric_amount(self):
        return self.v / 6.5 + 0.5


class Costume(Clothing):
    def __init__(self, h):
        self.h = h

    @property
    def fabric_amount(self):
        return 2 * self.h + 0.3


coat = Coat(2)
print(coat.fabric_amount)

costume = Costume(1.8)
print(costume.fabric_amount)
