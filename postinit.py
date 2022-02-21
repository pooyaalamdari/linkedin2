from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float

    # the __post_init__ function lets us customize additional properties
    # create a customize attribute, and it's name is description
    def __post_init__(self):
        self.description = f'{self.title} by {self.author}, {self.pages} pages.'


b1 = Book('War and Peace', 'Leo Tolstoy', 1225, 39.49)
b2 = Book('Criminal and Punishment', 'Feo Dostoevsky', 600, 29.90)

print(b1.description)
print(b2.description)
