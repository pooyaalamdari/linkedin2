class Book:
    def __init__(self, title, price, authorfname, authorlname):
        self.title = title
        self.price = price

        self.authorfname = authorfname
        self.authorlname = authorlname

        self.chapters = []


    def addchapter(self, name, pages):
        self.chapters.append((name, pages))

b1 = Book('War and peace', 39.0, 'Leo', 'Tolstoy')

b1.addchapter('Chapter1', 125)
b1.addchapter('Chapter2', 97)
b1.addchapter('Chapter', 143)

print(b1.title)
