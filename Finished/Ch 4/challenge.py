# Python Object Oriented Programming by Joe Marini course example
# Programming challenge: implement a dataclass

from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class Asset(ABC):
    price: float

    @abstractmethod
    def __lt__(self, other):
       pass
    

@dataclass
class Stock(Asset):
    ticker: str
    company: str

    def __lt__(self, other):
        return self.price < other.price

@dataclass
class Bond(Asset):
    description: str
    duration: int
    yieldamt: float

    def __lt__(self, other):
        return self.yieldamt < other.yieldamt


# ~~~~~~~~~ TEST CODE ~~~~~~~~~
stocks = [
    Stock(342.0, "MSFT", "Microsoft Corp"),
    Stock(135.0, "GOOG", "Google Inc"),
    Stock(275.0, "META", "Meta Platforms Inc"),
    Stock(120.0, "AMZN", "Amazon Inc")
]

bonds = [
    Bond(95.31, "30 Year US Treasury", 30, 4.38),
    Bond(96.70, "10 Year US Treasury", 10, 4.28),
    Bond(98.65, "5 Year US Treasury", 5, 4.43),
    Bond(99.57, "2 Year US Treasury", 2, 4.98)
]

try:
   ast = Asset(100.0)
except:
   print("Can't instantiate Asset!")

stocks.sort()
bonds.sort()

for stock in stocks:
    print(stock)
print("-----------")
for bond in bonds:
    print(bond)
