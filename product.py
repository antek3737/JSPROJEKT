import MyExceptions
from decimal import *
getcontext().prec=3

class Product:
    """has two field name:str , value:Decimal"""

    def __init__(self, name:str, value:str):

        value = Decimal(value)

        if value < 0:
            raise MyExceptions.IllegalValueException("Produkt ma niewłaściwą wartość.")
        self.__name = name
        self.__value = value

    def getName(self):
        return self.__name

    def getValue(self):
        return self.__value

    def __str__(self):
        return "{0} price {1}".format(self.getName(), self.getValue())

    def __hash__(self):
        return hash((self.getValue(), self.getName()))

    def __eq__(self, other):
        return (self.getValue() == other.getValue()) and (self.getName() == other.getName())

    def __ne__(self, other):
        return not (self == other)
