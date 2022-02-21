

class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price


# create some instances
b1 = Book('War and Peace', 'Leo Tolstoy', 1200, 59.39)
b2 = Book('Criminal and Punishment', 'Feo Dostoevsky', 800, 40)