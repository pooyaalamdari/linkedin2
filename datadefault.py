from dataclasses import dataclass, field
import random


def price_func():
    return float(random.randrange(20, 40))


@dataclass
class Book:
    # define default values
    title: str = 'No Title'
    author: str = 'No Author'
    pages: int = 0
    price: float = field(default_factory=price_func)


# define obj without argument
b1 = Book('Criminal and Punishment', 'Feo Dostoevsky', 600)
print(b1)
