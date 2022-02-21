class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price
        self._discount = 0.1

    def __str__(self):
        return f'{self.title} by {self.author} costs {self.price}'

    # __getattribute__ for retrieved attribute
    def __getattribute__(self, name):
        if name == 'price':
            p = super().__getattribute__('price')
            d = super().__getattribute__('_discount')
            return p - (p * d)
        return super().__getattribute__(name)


b1 = Book('War and Peace', 'Leo Tolstoy', 39.95)
b2 = Book('criminal and punishment', 'feodor dostayevsky', 40)

# 38.95 - (38.95 * 0.1)
b1.price = 38.95
print(b1)
print('------')
print(b1.price)