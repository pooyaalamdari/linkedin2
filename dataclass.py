from dataclasses import dataclass

@dataclass
class Book:
    title : str
    author : str
    pages : int
    price : float


# create some instances
b1 = Book('War and Peace', 'Leo Tolstoy', 1200, 59.39)
b2 = Book('Criminal and Punishment', 'Feo Dostoevsky', 800, 40.39)
b3 = Book('Go fuck yourself', 'write by me', 666, 85)
b4 = Book('Go fuck yourself', 'write by me', 666, 85)

# with dataclass we can print book itself!
print(b1)

# with dataclass we can compare objects together
print(b3 == b4)


# print(b1.title)
# print('------')
# print(b2.author)
# print('------')
# print(b3.price)

