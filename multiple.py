

class A:
    def __init__(self):
        super().__init__()
        self.foo = 'foo'
        self.name = 'Class A'


class B:
    def __init__(self):
        super().__init__()
        self.bar = 'bar'
        self.name = 'Class B'

# left to right
class C(B, A):
    def __init__(self):
        super().__init__()

    def showprops(self):
        print(self.foo)
        print(self.bar)
        print(self.name)


c = C()
c.showprops()

# which one comes first?
print(C.__mro__)