#create a basic class

class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        #add properties
        self.author = author
        self.pages = pages
        self.price = price

    # create instance methods
    def getprice(self):
        return self.price


#create a instance of the class
b1 = Book('Brave new world', 'John Doe', 385, 85.39)
b2 = Book('War and peace', 'Leo Tolstoy', 1225, 39.99)

#print class
print(b1)

#print property
print(b1.title)

#print method
print(b1.getprice())



