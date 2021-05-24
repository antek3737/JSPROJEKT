from decimal import *

getcontext().prec = 3
import MyExceptions
from random import randint


class Coin:
    """Has two fields: value:Decimal , currency:str"""

    def __init__(self, value: str, currency: str):
        value = Decimal(value)
        if value <= 0:
            raise MyExceptions.IllegalValueException("Moneta ma niewłaściwą wartość.")
        self.__value = value
        self.__currency = currency

    def __str__(self):
        if self.__value < 1:
            return "{0} gr ".format(self.__value)
        else:
            return "{0} zł ".format(self.__value)

    def __hash__(self):
        return hash((self.getValue(), self.getCurrency()))

    def __eq__(self, other):
        return (self.getValue() == other.getValue()) and (self.getCurrency() == other.getCurrency())

    def __ne__(self, other):
        return not (self == other)

    def getValue(self):
        return self.__value

    def getCurrency(self):
        return self.__currency


def coinsGenerator(n:int, currency: str):
    """return one Coin with random value, all values are same probably"""
    for c in range(n):
        luck = randint(0, 8)
        coinsToGenerate = {0: Coin("5", currency),
                           1: Coin("2", currency),
                           2: Coin("1", currency),
                           3: Coin("0.50", currency),
                           4: Coin("0.20", currency),
                           5: Coin("0.10", currency),
                           6: Coin("0.05", currency),
                           7: Coin("0.02", currency),
                           8: Coin("0.01", currency)}
        yield coinsToGenerate[luck]
