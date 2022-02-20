class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price

class Periodical(Publication):
    def __init__(self, title, price, period, publisher):
        super().__init__(title, price)
        self.period = period
        self.publisher = publisher

class Book(Publication):
    def __init__(self, title, author, pages, price):
        super().__init__(title, price)
        self.author = author
        self.pages = pages

class Magazine(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, publisher, price, period)

class Newspaper(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, publisher, price, period)

b1 = Book('Brave new world', 'Alex', 120, 99.99)
n1 = Newspaper('Economist', 'The economist', 80, 19.86)
m1 = Magazine('sites', 'Google', 300, 29.39)

print(b1.author)
print(n1.publisher)
print(b1.price, m1.price, n1.price)