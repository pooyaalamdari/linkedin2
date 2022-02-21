class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price


b1 = Book('war and zone', 'alex', 39)
b2 = Book('book2', 'person2', 49.99)
b3 = Book('war and zone', 'alex', 39)
b4 = Book('book4', 'person4', 50)

# check for equality
print(b1 == b3)

