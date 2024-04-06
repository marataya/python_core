class PriceControl:
    """
    Descriptor which don't allow to set price
    less than 0 and more than 100 included.
    """

    def __set__(self, instance, value):
        if not 0 <= value <= 100:
            raise ValueError('Price must be between 0 and 100.')
        instance.__dict__['price'] = value


class NameControl:
    """
    Descriptor which don't allow to change field value after initialization.
    """

    def __init__(self, name):
        self.name = name
        self.has_value = False

    def __set__(self, instance, value):
        if self.has_value:
            raise ValueError(f'{self.name} can not be changed')
        self.has_value = True
        self.value = value
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

class Book:
    author = NameControl('author')
    name = NameControl('name')
    price = PriceControl()

    def __init__(self, author, name, price):
        self.author = author
        self.name = name
        self.price = price


if __name__ == '__main__':
    b = Book("William Faulkner", "The Sound and the Fury", 12)
    print(f"Author='{b.author}', Name='{b.name}', Price='{b.price}'")
    # Author='William Faulkner', Name='The Sound and the Fury', Price='12'

    b.price = 55
    print(b.price)
    # 55
    b.price = -12  # => ValueError: Price must be between 0 and 100.
    b.price = 101  # => ValueError: Price must be between 0 and 100.

    b.author = "new author"  # => ValueError: Author can not be changed.
    b.name = "new name"  # => ValueError: Name can not be changed.
