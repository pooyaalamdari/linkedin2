class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    def __eq__(self, value):
        if not isinstance(value,Book):
            raise ValueError("Can't compare book to a non-book")
        return (self.title == value.title and
                self.author == value.author and
                self.price == value.price)

    # __ge__
    def __ge__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare book to a non-book")

        return self.price >= value.price

    # __lt__
    def __lt__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare book to a non-book")

        return self.price < value.price

b1 = Book('war and zone', 'alex', 39)
b2 = Book('book2', 'person2', 49.99)
b3 = Book('war and zone', 'alex', 39)
b4 = Book('book4', 'person4', 50)

# check for equality
print(b1 == b3)
print('------')

# check for greater and lesser (price)
print(b2 >= b1)
print(b2 < b1)







