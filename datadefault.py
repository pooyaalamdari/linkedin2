from dataclasses import dataclass


@dataclass
class Book:
    # define default values
    title: str = 'No Title'
    author: str = 'No Author'
    pages: int = 0
    price: float = 10.0 # default


# define obj without argument
b1 = Book('Criminal and Punishment', 'Feo Dostoevsky', 600)
print(b1)
