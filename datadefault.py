from dataclasses import dataclass


@dataclass
class Book:
    # define default values
    title: str = 'No Title'
    author: str = 'No Author'
    pages: int = 0
    price: float = 0.0


# define obj without argument
b1 = Book()
print(b1)
