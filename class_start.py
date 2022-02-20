class Book:

    # properties defined at the class level are shared by all instance
    BOOK_TYPES = ('HARDCOVER', 'PAPERBACK', 'EBOOK')

    # __properties are hidden from other classes (private)
    __booklist = None

    # create a class method
    @classmethod
    def getbooktypes(cls):
        return cls.BOOK_TYPES

    @staticmethod
    def getbooklist():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist

    def setTitle(self,newtitle):
        self.title = newtitle

    def __init__(self, title, booktype):
        self.title = title
        if (not booktype in Book.BOOK_TYPES):
            raise ValueError(f'{booktype} is not a valid book type')
        else:
            self.booktype = booktype

# TO DO = access the class attribute
print('Book types: ', Book.getbooktypes())

# Create some book instances
# we use this function --> def __init__(self, title, booktype)
b1 = Book('Title1', 'HARDCOVER')
# for example COMIC is NOT Valid book type
b2 = Book('Title2', 'PAPERBACK')

# use the static method
thebooks = Book.getbooklist()
thebooks.append(b1)
thebooks.append(b2)
print(thebooks)