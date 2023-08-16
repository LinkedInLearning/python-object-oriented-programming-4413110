# Python Object Oriented Programming by Joe Marini course example
# Programming challenge: use inheritance and abstract classes

from abc import ABC

class Asset(ABC):
    pass

class StockSymbol(Asset):
    pass

class Bond(Asset):
    pass
