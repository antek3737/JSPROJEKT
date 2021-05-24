
class IllegalValueException(Exception):
    def __init__(self, message):
        super().__init__(message)


class IllegalCurrencyException(Exception):
    def __init__(self, message):
        super().__init__(message)


class IllegalCoinException(Exception):
    def __init__(self, message):
        super().__init__(message)


class IllegalNumberOfProductsException(Exception):
    def __init__(self, message):
        super().__init__(message)

class IllegalAmountOfProductsException(Exception):
    def __init__(self, message):
        super().__init__(message)

