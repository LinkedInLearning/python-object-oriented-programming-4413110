# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions


# TODO: create a basic class
# The __init__ is also known as the initializer function in Python. 
# It is the first thing that is called in a class before other functions.
class Book:
  def __init__(self, title):
    self.title = title

# TODO: create instances of the class
book1 = Book("Brave New World")
book2 = Book("War and Peace")

# TODO: print the class and property
print(book1)
print(book1.title)