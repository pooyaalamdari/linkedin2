

class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    # use the __str__ method to return a string
    def __str__(self):
        return f'{self.title} by {self.author}, costs {self.price}'

    # use the __repl__ method
    def __repr__(self):
        return f'title={self.title}, author={self.author}, price={self.price}'



b1 = Book('War and Peace', 'Leo Tolstoy', 99.39)
b2 = Book('book example 2', 'John Doe', 9)

print(b1)
print(b2)
print(str(b1))
print(repr(b2))
