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

b1 = Book('war and zone', 'alex', 39)
b2 = Book('book2', 'person2', 49.99)
b3 = Book('war and zone', 'alex', 39)
b4 = Book('book4', 'person4', 50)

# check for equality
print(b1 == b3)
print('------')

# example for isinstance
x = isinstance(5, int)
print(x)
print('------')

class MyObj:
    name = 'John'

y = MyObj()
x = isinstance(y, MyObj)
print(x)





