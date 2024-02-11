# Python Object Oriented Programming by Joe Marini course example
# Understanding class inheritance
# The start of the code had each class having title, price each separately.

# We start by creating a class called Publication and include title and price that are
# common to other classes.
class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price
        
# Since the magazines also use title and price but have other duplicate classes. 
# We can build a Peridical class and inherit Publication with title and price.
class Periodical(Publication):
    def __init__(self, title, price, period, publisher):
        super().__init__(title, price)
        self.period = period
        self.publisher = publisher

# After the Publication class is built we update the other classes to inherit it.
# To inherit the Publication class for our book class we put it into parenthesis.
class Book(Publication):
    def __init__(self, title, author, pages, price):
        super().__init__(title, price)
        self.author = author
        self.pages = pages

class Magazine(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price, period, publisher)


class Newspaper(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price, period, publisher)


b1 = Book("Brave New World", "Aldous Huxley", 311, 29.0)
n1 = Newspaper("NY Times", "New York Times Company", 6.0, "Daily")
m1 = Magazine("Scientific American", "Springer Nature", 5.99, "Monthly")

print(b1.author, b1.pages)
print(n1.publisher)
print(b1.price, m1.price, n1.price)
