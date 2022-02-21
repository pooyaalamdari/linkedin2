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

print(b1.title)
print('------')
print(b2.author)

