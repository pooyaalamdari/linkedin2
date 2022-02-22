from dataclasses import dataclass


@dataclass(frozen=True)  # the frozen parameter makes the class immutable
class ImmutableClass:
    value1: str = 'Value1'
    value2: int = 0

    def somefunc(self, newval):
        self.value2 = newval

obj = ImmutableClass()
print(obj.value1)

# if we run we got an error
obj.value1 = 'Another value'
print(obj.value1)

# if run we got an Error again 
obj.somefunc(123)

