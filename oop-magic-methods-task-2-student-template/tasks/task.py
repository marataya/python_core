class Bird:
    def __init__(self, name):
        self.name = name


    def fly(self):
        return "Any bird can fly"

    def walk(self):
        return "Any bird can walk"


class FlyingBird(Bird):
    def __init__(self, name, ration='grains'):
        super().__init__(name)
        self.ration = ration

    def eat(self):
        return f'It eats mostly {self.ration}'

    def __str__(self):
        return f"{self.name} bird can walk and fly"

class NonFlyingBird(Bird):

    def fly(self):
        raise AttributeError(f'{self.name} object has no attribute \'fly\'')

    def __init__(self, name, ration='fish'):
        super().__init__(name)
        self.ration = ration

    def swim(self):
        return f'{self.name} bird can swim'

    def eat(self):
        return f'It eats mostly {self.ration}'


class SuperBird(NonFlyingBird, FlyingBird):
    def __str__(self):
        return f"{self.name} bird can walk, swim and fly"

if __name__ == '__main__':
    b = Bird("Any")
    print(b.walk())
    # "Any bird can walk"

    p = NonFlyingBird("Penguin", "fish")
    print(p.swim())
    # "Penguin bird can swim"
    # print(p.fly())
    # AttributeError: 'Penguin' object has no attribute 'fly'
    print(p.eat())
    # "It eats mostly fish"

    c = FlyingBird("Canary")
    print(str(c))
    # "Canary bird can walk and fly"
    print(c.eat())
    # "It eats mostly grains"

    s = SuperBird("Gull")
    print(str(s))
    # "Gull bird can walk, swim and fly"
    print(s.eat())
    # "It eats mostly fish"
