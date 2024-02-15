# Python Object Oriented Programming by Joe Marini course example
# implementing default values in data classes

# TODO: Import "field" function from dataclasses
from dataclasses import dataclass

# TODO: Define a function that returns a random number between 20-40.
# Don't forget to import the necessary module


@dataclass
class Book:
    # you can define default values when attributes are declared
    title: str
    author: str
    pages: int
    price: float
    # TODO: Use the field function to get default price as random number
