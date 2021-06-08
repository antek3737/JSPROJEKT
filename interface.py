
from automat import Automat
from tkinter import *
from tkinter import ttk

automat = Automat("PLN")

window = Tk()
window.title("Automat")
window.configure(background="black")
mainframe = ttk.Frame(window)
mainframe.grid(column=4, row=3)


def printNumber(var_number, n):
    automat.chooseNumber(str(n))
    var_number.set(automat.getChosenNumber())

def printProducts(var_temp):
    var_temp.set(automat.returnPrettyListOfProducts())


def printPrice(var_temp):
    var_temp.set(automat.getChosenProductPrice())


def selectProduct(var_temp):
    var_temp.set(automat.selectNumber())


def putCoin(var_temp, coin):
    var_temp.set(automat.putCoin(coin))


def resign(var_temp):
    var_temp.set(automat.resignOfTransaction())


var_number = StringVar()
var_temp = StringVar()
var_products = StringVar()

nextFreeRow = 0
label_info = Label(window,
                   textvariable=var_temp,
                   justify=CENTER,
                   foreground="white",
                   background="black",
                   relief=SUNKEN,
                   font=90,
                   width=40,
                   height=30
                   ).grid(row=0, columnspan=3)


nextFreeRow += 1

label_number = Label(window,
                     textvariable=var_number,
                     justify=CENTER,
                     foreground="white",
                     background="black",
                     relief=SUNKEN,
                     font=90,
                     width=30,
                     height=4,
                     ).grid(row=1, columnspan=3)
nextFreeRow += 1

# Numpad
n = 1
for i in range(3):
    Button(window, text=n, width=10, command=lambda n=n: printNumber(var_number, n)) \
        .grid(row=nextFreeRow, column=0, columnspan=1,sticky="nsew")
    Button(window, text=n + 1, width=10, command=lambda n=n + 1: printNumber(var_number, n)) \
        .grid(row=nextFreeRow, column=1, columnspan=1,sticky="nsew")
    Button(window, text=n + 2, width=10, command=lambda n=n + 2: printNumber(var_number, n)) \
        .grid(row=nextFreeRow, column=2, columnspan=1,sticky="nsew")
    nextFreeRow += 1
    n += 3

Button(window, text=0, width=30 , command=lambda n=0: printNumber(var_number, n)) \
    .grid(row=nextFreeRow, column=0, columnspan=3)

nextFreeRow += 1

# Sprawdz cene, wybierz produkt
Button(window, text="Sprawdz\ncene", width=20, command=lambda: printPrice(var_temp)) \
    .grid(row=nextFreeRow, column=0, columnspan=2,sticky="nsew")

Button(window, text="Wybierz\nprodukt", width=10, command=lambda: selectProduct(var_temp)) \
    .grid(row=nextFreeRow, column=2, columnspan=1,sticky="nswe")

nextFreeRow += 1

# Generowanie przyciskow odpowiadajacych za monety
listOfCoins = automat.getProperCoins()
n = 0
for i in range(3):
    Button(window, text=listOfCoins[n], width=10, command=lambda coin=listOfCoins[n]: putCoin(var_temp, coin)) \
        .grid(row=nextFreeRow, column=0, columnspan=1,sticky="nsew")
    Button(window, text=listOfCoins[n + 1], width=10, command=lambda coin=listOfCoins[n + 1]: putCoin(var_temp, coin)) \
        .grid(row=nextFreeRow, column=1, columnspan=1,sticky="nsew")
    Button(window, text=listOfCoins[n + 2], width=10, command=lambda coin=listOfCoins[n + 2]: putCoin(var_temp, coin)) \
        .grid(row=nextFreeRow, column=2, columnspan=1,sticky="nsew")
    n += 3
    nextFreeRow += 1

Button(window, text="ZREZYGNUJ", width=30, command=lambda: resign(var_temp)) \
    .grid(row=nextFreeRow, column=0, columnspan=3,sticky="nsew")

nextFreeRow += 1
Button(window, text="Wyswietl", width=30, command=lambda: printProducts(var_temp)) \
    .grid(row=nextFreeRow, column=0, columnspan=3,sticky="nsew")


window.mainloop()
