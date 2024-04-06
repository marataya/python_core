from __future__ import annotations
from typing import Type


class Currency:
    """
    1 EUR = 2 USD = 100 GBP

    1 EUR = 2 USD    ;  1 EUR = 100 GBP
    1 USD = 0.5 EUR  ;  1 USD = 50 GBP
    1 GBP = 0.02 USD ;  1 GBP = 0.01 EUR
    """
    EXCHANGE_RATES = {
        'Euro': {'Dollar': 2.0, 'Pound': 1 / 0.01, 'Euro': 1.0},
        'Dollar': {'Euro': 1 / 2, 'Pound': 1 / 0.02, 'Dollar': 1.0},
        'Pound': {'Euro': 0.01, 'Dollar': 0.02, 'Pound': 1.0},
    }

    def __init__(self, value: float):
        self.value = value

    def __str__(self):
        """Returns a string representation of the currency."""
        return f"{self.value} {Currency.ticker(self.__class__.__name__)}"

    @staticmethod
    def ticker(class_name):
        ticker = ""
        match class_name:
            case 'Euro':
                ticker = 'EUR'
            case 'Dollar':
                ticker = 'USD'
            case 'Pound':
                ticker = 'GBP'
        return ticker

    @classmethod
    def course(cls, other_cls: Type[Currency]) -> str:
        """Returns the exchange rate as a string."""
        rate = cls.EXCHANGE_RATES[cls.__name__][other_cls.__name__]
        return f"{rate} {Currency.ticker(other_cls.__name__)} for 1 {Currency.ticker(cls.__name__)}"

    def to_currency(self, other_cls: Type[Currency]):
        """Convert the currency to target currency"""
        rate = self.EXCHANGE_RATES[self.__class__.__name__][other_cls.__name__]
        return other_cls(self.value * rate)

    def __add__(self, other):
        """Adds two currencies and returns sum in 1st currency"""
        second_arg = None
        if not isinstance(self, other.__class__):
            rate = self.EXCHANGE_RATES[other.__class__.__name__][self.__class__.__name__]
            second_arg = self.__class__(other.value * rate)
        else:
            second_arg = other
        return self.__class__(self.value + second_arg.value)

    def __gt__(self, other):
        """Compares two currencies of the same type."""
        if not isinstance(self, other.__class__):
            raise TypeError("Can only compare currencies of the same type")
        return self.value > other.value

    def __lt__(self, other):
        """Compares two currencies of the same type."""
        if not isinstance(self, other.__class__):
            raise TypeError("Can only compare currencies of the same type")
        return self.value < other.value

    def __eq__(self, other):
        """Compares two currencies of the same type."""
        if not isinstance(self, other.__class__):
            return False
        return self.value == other.value


class Euro(Currency):
    pass


class Dollar(Currency):
    pass


class Pound(Currency):
    pass


if __name__ == '__main__':
    # course - classmethod which returns string in the following pattern: {float value} {currency to} for 1 {currency for}

    print(
        f"Euro.course(Pound)   ==> {Euro.course(Pound)}\n"
        f"Dollar.course(Pound) ==> {Dollar.course(Pound)}\n"
        f"Pound.course(Euro)   ==> {Pound.course(Euro)}\n"
    )
    # Euro.course(Pound)   ==> 100.0 GBP for 1 EUR
    # Dollar.course(Pound) ==> 50.0 GBP for 1 USD
    # Pound.course(Euro)   ==> 0.01 EUR for 1 GBP

    e = Euro(100)
    r = Pound(100)
    d = Dollar(200)

    # e = 100 EUR
    # e.to_currency(Dollar) = 200.0 USD  # Dollar instance printed
    # e.to_currency(Pound) = 10000.0 GBP  # Pound instance printed
    # e.to_currency(Euro)   = 100.0 EUR  # Euro instance printed

    print(
        f"r = {r}\n"
        f"r.to_currency(Dollar) = {r.to_currency(Dollar)}\n"
        f"r.to_currency(Euro)   = {r.to_currency(Euro)}\n"
        f"r.to_currency(Pound) = {r.to_currency(Pound)}\n"
    )
    # r = 100 GBP
    # r.to_currency(Dollar) = 2.0 USD  # Dollar instance printed
    # r.to_currency(Euro)   = 1.0 EUR  # Euro instance printed
    # r.to_currency(Pound) = 100.0 GBP  # Pound instance printed

    # - `+` - returns an instance of a new value

    e = Euro(100)
    r = Pound(100)
    d = Dollar(200)
    print(
        f"e + r  =>  {e + r}\n"
        f"r + d  =>  {r + d}\n"
        f"d + e  =>  {d + e}\n"
    )
    # e + r  =>  101.0 EUR  # Euro instance printed
    # r + d  =>  10100.0 GBP  # Pound instance printed
    # d + e  =>  400.0 USD  # Dollar instance printed
