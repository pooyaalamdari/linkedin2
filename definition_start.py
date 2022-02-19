#create a basic class
class Book:
    def __init__(self, title):
        self.title = title

#create a instance of the class
b1 = Book('Brave new world')
b2 = Book('War and peace')

#print class
print(b1)

#print property
print(b1.title)