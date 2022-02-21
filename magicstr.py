

class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price



b1 = Book('War and Peace', 'Leo Tolstoy', 99.39)
b2 = Book('book example 2', 'John Doe', 9)

print(b1)
print(b2)
