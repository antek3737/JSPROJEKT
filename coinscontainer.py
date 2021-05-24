from random import randint

import MyExceptions
from decimal import *

getcontext().prec = 3
from coin import Coin


class CoinsContainer:
    """class has two fields: currency:str, Dictionary(Coin : amount:int) """

    def __init__(self, currency: str):
        self.__currency = currency
        self.__dictOfCoins = {Coin("5", currency): 0,
                              Coin("2", currency): 0,
                              Coin("1", currency): 0,
                              Coin("0.50", currency): 0,
                              Coin("0.20", currency): 0,
                              Coin("0.10", currency): 0,
                              Coin("0.05", currency): 0,
                              Coin("0.02", currency): 0,
                              Coin("0.01", currency): 0}

    def __str__(self):
        listOfCoinsWithTheirAmounts = self.getListOfCoinsWithAmountsFromCoinsContainer()
        txt = str()
        for tab in listOfCoinsWithTheirAmounts:
            txt += tab + "\n"
        return txt

    def addCoin(self, coin: Coin):
        """adds coin to dictionary and increases amount +1 """

        if coin in self.getDictOfCoins().keys():
            self.getDictOfCoins()[coin] = self.getDictOfCoins()[coin] + 1

        elif coin.getCurrency() != self.__currency:
            raise MyExceptions.IllegalCurrencyException("Moneta ma inna walute niż zdefiniowana w CoinsContainer")

    def addToSelfFromAnother(self, other):
        for coin, amount in other.getDictOfCoins().items():
            for i in range(amount):
                self.addCoin(coin)

    def substractSelfWithAnother(self, other):
        for coin, amount in other.getDictOfCoins().items():
            self.__dictOfCoins[coin] = self.__dictOfCoins[coin] - amount

    def inputListOfCoins(self, coins: list):
        """adds all coins from list of coins"""
        for c in coins:
            self.addCoin(c)

    def getSumOfValuesOfCoins(self):
        """returns sum of all coins in container"""
        sum = Decimal('0')
        for c, amount in self.getDictOfCoins().items():
            sum += Decimal(c.getValue()) * Decimal(str(amount))
        return Decimal(sum)

    def eraseContainer(self):
        for coin in self.__dictOfCoins.keys():
            self.__dictOfCoins[coin] = 0

    def getDictOfCoins(self):
        """returns Dictionary(Coin : amount:int)"""
        return self.__dictOfCoins

    def getListOfCoinsWithAmountsFromCoinsContainer(self):
        """return a list of coins with amounts from container"""
        listOfCoinsWithTheirAmounts = list()
        for c, amount in self.getDictOfCoins().items():
            listOfCoinsWithTheirAmounts.append("{0} {1} szt.".format(c, amount))
        return listOfCoinsWithTheirAmounts

    def getCurrency(self):
        return self.__currency

    def getListOfCoins(self):
        listOfCoins = [coin for coin in self.getDictOfCoins().keys()]
        return listOfCoins

    @staticmethod
    def generateListOfCoins(n: int, currency: str):
        listOfGeneratedCoins = list()
        for i in range(n):
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
            listOfGeneratedCoins.append(coinsToGenerate[luck])
        return listOfGeneratedCoins
