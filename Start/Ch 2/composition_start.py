# Python Object Oriented Programming by Joe Marini course example
# Using composition to build complex objects

#TODO: Arrange the composition of the Book class to operate on subclasses
class Book:
    def __init__(self, title, price, authorfname, authorlname):
        self.title = title
        self.price = price

        self.authorfname = authorfname
        self.authorlname = authorlname

        self.chapters = []

    def addchapter(self, name, pages):
        self.chapters.append((name, pages))

     #TODO: Method for counting the total number of pages from all chapters

#TODO: Create classes "Chapter"(with attributes "name" and "pages")
# and "Author" with ("fname" and "lname") and a method __str__ returning author details


#TODO: Create an author object and add it to the book

b1 = Book("War and Peace", 39.0, "Leo", "Tolstoy")

b1.addchapter("Chapter 1", 125)
b1.addchapter("Chapter 2", 97)
b1.addchapter("Chapter 3", 143)

print(b1.title)
