import MyExceptions
from product import Product


class ProductsContainer:
    """has one field:  list which contains in following order [Product , amount:str, index:str  ] """

    def __init__(self):
        self.assignedList = list()

    def __str__(self):
        """returns """
        listOfProductsWithAmountAndIndexes = str()
        for i in self.assignedList:
            listOfProductsWithAmountAndIndexes += "Product: {0} Amount :{1}\n Index:{2}\n".format(i[0], i[1], i[2])
        return listOfProductsWithAmountAndIndexes

    def inputListOfProducts(self, listOfProducts):
        """Changes list of products into list which contains in following order [Product , amount:str, index:str ] """
        if len(listOfProducts) > 20 + 1 or len(listOfProducts) < 0:
            raise MyExceptions.IllegalNumberOfProductsException(
                "Lista zawiera zbyt dużo produktów lub nie zawiera ich wcale.")
        else:
            for i, p in enumerate(listOfProducts):
                p.append(str(i + 30))
                self.assignedList.append(p)

    def getListOfProductsWithAmountAndIndexes(self):
        """Returns list which contains in following order [Product , amount:int, index:str ] """
        return self.assignedList

    def getPrettyListOfProductsWithIndexed(self):
        temp = "Produkty\n"
        for tab in self.assignedList:
            temp += "{0}. {1}\n".format(tab[2], tab[0])
        return temp

    @staticmethod
    def getListOfProductsWithPricesAndIndexesFromFile(path="listOfProductsWithPriceAndAmount"):
        file = open(path, mode="r", encoding="utf-8")
        productsToInput = list()
        for line in file:
            strTab = line.split(',')
            productsToInput.append([Product(strTab[0], strTab[1]), int(strTab[2])])
        file.close()
        return productsToInput
