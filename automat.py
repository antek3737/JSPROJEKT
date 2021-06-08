import copy
from decimal import *

getcontext().prec = 3
from coinscontainer import CoinsContainer
from productscontainer import ProductsContainer


class Automat:
    """has five  fields coinsContainer:CoinsContainer ,productsInAutomat:ProductsContainer
    clientsMoney:CoinsContainer chosen:str remainder:Decimal """

    def __init__(self, currency: str):
        self.__coinsInAutomat = CoinsContainer(currency)
        self.__coinsInAutomat.inputListOfCoins(CoinsContainer.generateListOfCoins(100, currency))

        self.__productsInAutomat = ProductsContainer()
        self.__productsInAutomat.inputListOfProducts(ProductsContainer.getListOfProductsWithPricesAndIndexesFromFile())

        self.__clientsCoins = CoinsContainer(currency)
        self.__chosen = str()
        self.__remainderContainer = CoinsContainer(currency)

    def chooseNumber(self, number: str):
        if len(self.__chosen) == 2:
            temp = copy.deepcopy(self.__chosen)
            del self.__chosen
            self.__chosen = number
            self.__chosen += temp[0]
        else:
            self.__chosen += number
        #print(self.__chosen)
        return self.__chosen

    def selectNumber(self):
        if not self.__isNumberCorrect():
            return "Wybrano zły numer"
        if not self.__isProductAvailable():
            return "Produkt niedostepny"
        if not self.__isEnoughCoinsToBuyProduct():
            return "Brakuje jeszcze: {0}".format(self.getChosenProductPrice() - self.__getSumOfClientsCoins())
        else:
            if not self.__isRemainderToGetPossible(str(self.__getSumOfClientsCoins() - self.getChosenProductPrice())):
                return "Tylko odliczona kwota"
            else:
                # dodaje do automatu monety klienta
                self.__coinsInAutomat.addToSelfFromAnother(self.__clientsCoins)
                self.__clientsCoins.eraseContainer()

                # odejmuje od monet w automacie reszte
                self.__coinsInAutomat.substractSelfWithAnother(self.__remainderContainer)

                # zwracam reszte i produkt
                temp = copy.deepcopy(self.__remainderContainer)
                self.__remainderContainer.eraseContainer()
                print(temp.getListOfCoinsWithAmountsFromCoinsContainer())
                return "Kupiono: {0} \n".format(str(self.getChosenProduct().getName())), temp

    def getChosenNumber(self):
        return self.__chosen

    def __isNumberCorrect(self):
        if not self.__chosen:
            return False
        if int(self.__chosen) < 30 or int(self.__chosen) > 50:
            return False
        return True

    def getChosenProduct(self):
        for subList in self.__productsInAutomat.getListOfProductsWithAmountAndIndexes():
            if self.__chosen == subList[2]:
                subList[1] = subList[1] - 1
                return subList[0]

    def getChosenProductPrice(self):
        if not self.__isNumberCorrect():
            return "Wybrano zły numer"
        if not self.__isProductAvailable():
            return "Produkt niedostepny"
        for subList in self.__productsInAutomat.getListOfProductsWithAmountAndIndexes():
            if self.__chosen == subList[2]:
                return subList[0].getValue()

    def resignOfTransaction(self):
        "Aborts transaction and returns remainder as a coinsContainer"
        self.__chosen = str()
        temp = copy.deepcopy(self.__clientsCoins)
        self.__clientsCoins.eraseContainer()
        return temp

    def __isProductAvailable(self):
        if self.__isNumberCorrect():
            for subList in self.__productsInAutomat.getListOfProductsWithAmountAndIndexes():
                if self.__chosen == subList[2] and subList[1] > 0:
                    return True
        return False

    def __getSumOfClientsCoins(self):
        return self.__clientsCoins.getSumOfValuesOfCoins()

    def __getSumOfAutomatsCoins(self):
        return self.__coinsInAutomat.getSumOfValuesOfCoins()

    def __isEnoughCoinsToBuyProduct(self):
        return self.__getSumOfClientsCoins() >= self.getChosenProductPrice()

    def putCoin(self, coin):
        self.__clientsCoins.addCoin(coin)
        return "Wrzucono : {0}".format(self.__getSumOfClientsCoins())

    def __isRemainderToGetPossible(self, change):
        if Decimal(change) == 0:
            return True
        for coin, amount in self.__coinsInAutomat.getDictOfCoins().items():
            for a in range(amount):
                if self.__remainderContainer.getSumOfValuesOfCoins() + coin.getValue() <= Decimal(change):
                    self.__remainderContainer.addCoin(coin)
                    a -= 1
                else:
                    break
        if self.__remainderContainer.getSumOfValuesOfCoins() == Decimal(change):
            return True
        self.__remainderContainer.eraseContainer()
        return False

    def getProperCoins(self):
        """Returns list of coins proper to use in automat"""
        return self.__coinsInAutomat.getListOfCoins()
