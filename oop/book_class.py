# Book class that incorporates constructors (__init__), destructors (__del__), and the representation methods (__str__ and __repr__)

class Book:
    def __init__(self, title, author, year):     #Constructor
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):        #String representation
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):        #Official representation
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):         #Destructor
        print(f"Deleting {self.title}")
        