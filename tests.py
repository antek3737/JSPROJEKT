import unittest
from decimal import *

from coin import Coin

getcontext().prec = 3
from automat import Automat


class TestAutomat(unittest.TestCase):

    def test_shouldReturnPriceForCheckCommand_WhenTheNumberIsCorrect(self):
        """1. Sprawdzenie ceny jednego towaru - oczekiwana informacja o cenie."""
        # given
        automat = Automat("PLN")
        automat.chooseNumber("4")
        automat.chooseNumber("0")
        # sok gruszkowy , 3.75, numer w automacie: 40

        # when
        price = automat.getChosenProductPrice()

        # then
        self.assertEqual(price, Decimal("3.75"))

    def test_shouldReturnTrue_whenThereIsNoRemainderLeft(self):
        """2. "Wrzucenie odliczonej kwoty,zakup towaru - oczekiwany brak reszty."""
        # given
        automat = Automat("PLN")
        c1 = Coin("2.00", "PLN")
        c2 = Coin("1.00", "PLN")
        c3 = Coin("0.50", "PLN")
        c4 = Coin("0.20", "PLN")
        c5 = Coin("0.05", "PLN")
        automat.putCoin(c2)
        automat.putCoin(c3)
        automat.putCoin(c4)
        automat.putCoin(c1)
        automat.putCoin(c5)
        # suma 3.75

        automat.chooseNumber("4")
        automat.chooseNumber("0")
        # wybrany produkt:  sok gruszkowy , 3.75

        # when
        remainder = automat.selectNumber()[1].getSumOfValuesOfCoins()

        # then
        self.assertTrue(remainder.is_zero())

    def test_shouldReturnFalse_whenThereIsRemainderToLeft(self):
        """3.  Wrzucenie większej kwoty,zakup towaru - oczekiwana reszta."""
        # given
        automat = Automat("PLN")
        c1 = Coin("5.00", "PLN")
        automat.putCoin(c1)
        # suma 5.00

        automat.chooseNumber("4")
        automat.chooseNumber("0")
        # wybrany produkt:  sok gruszkowy , 3.75

        # when
        remainder = automat.selectNumber()[1].getSumOfValuesOfCoins()

        # then

        self.assertFalse(remainder.is_zero())

    def shouldReturnMsg_whenProductIsUnavailable(self):
        """4. Wykupienie całego asortymentu, próba zakupu po wyczerpaniu towaru oczekiwana informacja o braku."""
        # given
        automat = Automat("PLN")
        c1 = Coin("2.00", "PLN")
        c2 = Coin("1.00", "PLN")
        c3 = Coin("0.50", "PLN")
        c4 = Coin("0.20", "PLN")
        c5 = Coin("0.05", "PLN")

        # when
        # wykupienie calego asortymentu
        for _ in range(5):
            automat.putCoin(c2)
            automat.putCoin(c3)
            automat.putCoin(c4)
            automat.putCoin(c1)
            automat.putCoin(c5)
            automat.selectNumber()
        # then
        automat.putCoin(c2)
        automat.putCoin(c3)
        automat.putCoin(c4)
        automat.putCoin(c1)
        automat.putCoin(c5)
        msg = automat.selectNumber()

        self.assertEqual(msg, "Produkt niedostepny")

    def test_shouldReturnErrorMessage_whenSelectedProductToCheckPriceIsInvalid(self):
        """5. Sprawdzenie ceny towaru o nieprawidłowym numerze (<30lub >50) - oczekiwana informacja o błędzie."""
        automat = Automat("PLN")
        automat.chooseNumber("5")
        automat.chooseNumber("5")
        # niewłaściwy numer 55

        # when
        msg = automat.getChosenProductPrice()

        # then
        self.assertEqual(msg, "Wybrano zły numer")

    def shouldReturnRemainder_whenTransactionIsAborted(self):
        """Wrzucenie kilku monet, przerwanie transakcji - oczekiwany zwrot monet."""
        # given
        automat = Automat("PLN")
        c1 = Coin("2.00", "PLN")
        c2 = Coin("1.00", "PLN")
        c3 = Coin("0.50", "PLN")
        c4 = Coin("0.20", "PLN")
        c5 = Coin("0.05", "PLN")
        automat.putCoin(c2)
        automat.putCoin(c3)
        automat.putCoin(c4)
        automat.putCoin(c1)
        automat.putCoin(c5)
        # suma 3.75

        automat.chooseNumber("4")
        automat.chooseNumber("0")
        # wybrany produkt:  sok gruszkowy , 3.75

        # when
        remainder = automat.resignOfTransaction()

        # then

        self.assertTrue(not remainder.is_zero(), remainder.getSumOfValuesOfCoins() == Decimal("3.75"))

    def test_shouldLetBuyProduct_whenNumberIsReselected(self):
        """7. Wrzucenie za małej kwoty,wybranie poprawnego numeru towaru,
              wrzucenie reszty monet do odliczonej   kwoty,
              ponowne wybranie poprawnego numeru towaru
              - oczekiwany brak reszty."""
        # given
        automat = Automat("PLN")
        automat.chooseNumber("4")
        automat.chooseNumber("0")

        c1 = Coin("2.00", "PLN")
        c2 = Coin("1.00", "PLN")
        automat.putCoin(c1)
        automat.putCoin(c2)
        automat.selectNumber()

        # when
        c3 = Coin("0.50", "PLN")
        c4 = Coin("0.20", "PLN")
        c5 = Coin("0.05", "PLN")
        automat.putCoin(c3)
        automat.putCoin(c4)
        automat.putCoin(c5)
        remainder = automat.selectNumber()[1].getSumOfValuesOfCoins()
        # then

        self.assertTrue(remainder.is_zero())

    def test_shouldReturnTrue_whenCountingIsAppropriate(self):
        """"8. Zakup towaru płacąc po 1gr - 
        suma stu monet ma być równa 1zł.
        Płatności można dokonać za pomocą pętlifor w interpreterze.""""

        # given
        automat = automat("PLN")
        automat.chooseNumber("4")
        automat.chooseNumber("0")
        c1 = Coin("0.01", "PLN")

        # when
        for _ in range(100):
            automat.putCoin(c1)

        remainder = automat.resignOfTransaction().getSumOfValuesOfCoins()
        # then
        self.assertTrue(remainder, Decimal("1.00"))
