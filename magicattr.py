class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price
        self._discount = 0.1

    def __str__(self):
        return f'{self.title} by {self.author} costs {self.price}'


b1 = Book('War and Peace', 'Leo Tolstoy', 39.29)
b2 = Book('criminal and punishment', 'feodor dostayevsky', 40)
