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
        if hasattr(self, '_discount'):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def setdiscount(self, amount):
        self._discount = amount

#create a instance of the class
b1 = Book('Brave new world', 'John Doe', 385, 85.39)
b2 = Book('War and peace', 'Leo Tolstoy', 1225, 39.99)

# #print class
# print(b1)
# #print property
# print(b1.title)
# #print method
# print(b1.getprice())

#setting discount
print('before discount')
print(b2.getprice())
print('amount of discount = 0.25')
b2.setdiscount(0.25)
print('after discount')
print(b2.getprice())


