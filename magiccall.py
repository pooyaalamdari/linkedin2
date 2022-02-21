class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f'{self.title} by {self.author}, costs {self.price}'

    # the __call__ method can be used to call object like a function
    def __call__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price


b1 = Book('war and peace', 'leo tolstoy', 39.95)
b2 = Book('the second book', 'john doe', 29.95)
# if we do this we got an error
# 🖇
b3 = Book()


print(b1)
print('------')
b1('criminal and punishment', 'feodor dostayevsky', 44)
print(b1)
print('------')

# 🖇
b3('old man and sea', 'ernest hamming', 13.49)
print(b3)
