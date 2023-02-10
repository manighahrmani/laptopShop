from tkinter import *
from backend import ShoppingCart

mainWin = Tk()
cart = ShoppingCart()


def setupCart():
    """
    Add some products to the cart.
    """
    cart.addLaptop("Apple", "MacBook Air", 999.99)
    cart.addLaptop("Razer", "Blade", 1799.99)
    cart.addLaptop("Microsoft", "Surface", 900.00)


def setupMainWin():
    """
    Setup `mainWin` to display the cart.
    Display a button that lists all products and a button that closes `mainWin`.
    """
    mainWin.title("Cart")
    mainWin.geometry("300x50")
    mainWin.resizable(False, False)
    mainWin.columnconfigure(index=0, weight=4)

    listBtn = Button(mainWin, text="List all products", command=listProducts)
    listBtn.grid(row=0, column=0, padx=15, pady=10, sticky="w")

    quitBtn = Button(mainWin, text="Quit", command=mainWin.destroy)
    quitBtn.grid(row=0, column=1, padx=15, pady=10, sticky="e")

    mainWin.mainloop()


def listProducts():
    """
    For each product in `cart`, create a text and a button on the `mainWin`.
    The text contains the product's information.
    The button is used to configure the product.
    Also display the total price of the cart at the bottom of `mainWin`.
    """
    numberOfProds = cart.getCartLength()
    height = 50 * (numberOfProds + 2)
    mainWin.geometry("400x{}".format(height))

    productIndex = 1
    for product in cart.getItems():
        mainWin.rowconfigure(index=productIndex+1, weight=1)

        productTxt = Text(mainWin, height=2, width=50)
        productTxt.insert("1.0", str(product))
        productTxt.grid(row=productIndex + 1, column=0,
                        padx=10, pady=5, sticky="w")

        def configCmd():
            configWindow(product)

        configBtn = Button(mainWin, text="Configure", command=configCmd)
        configBtn.grid(row=productIndex + 1, column=1, padx=10, pady=5)

    totalLabel = Label(mainWin, text="Total: £{:.2f}".format(cart.getTotal()))
    totalLabel.grid(row=numberOfProds + 1, column=0,
                    padx=15, pady=10, sticky="w")
    totalLabel.config(font=("TkDefaultFont", 12, "bold"))


def configWindow(product):
    """
    Create a new window to configure the `product`.
    The window will contain a text, showing the product's information,
    The window will also contain an entry to change the RAM capacity.
    When the change is submitted, the list of products in `mainWin` will update.
    """
    configWin = Toplevel()
    configWin.geometry("400x150")
    configWin.resizable(False, False)

    configWin.title("Configure {} {}".format(
        product.getBrand(), product.getModel()))

    prodTxt = Text(configWin, height=2, width=45)
    prodTxt.insert("1.0", "Configure {}".format(product))
    prodTxt.grid(row=0, column=0, padx=15, pady=5, columnspan=2)

    ramLabel = Label(configWin, text="Enter RAM capacity (GB):")
    ramLabel.grid(row=1, column=0, padx=10, pady=10)

    ramEntry = Entry(configWin)
    ramEntry.insert(0, str(product.getRam()))
    ramEntry.grid(row=1, column=1, padx=10, pady=10)

    cancelBtn = Button(configWin, text="Cancel", command=configWin.destroy)
    cancelBtn.grid(row=2, column=0, padx=10, pady=10)

    def submitCmd():
        newRam = int(ramEntry.get())
        product.setRam(newRam)
        listProducts()
        configWin.destroy()

    submitBtn = Button(configWin, text="Submit", command=submitCmd)
    submitBtn.grid(row=2, column=1, padx=10, pady=2)

    configWin.mainloop()


def main():
    setupCart()
    setupMainWin()
    print("Cart is closed, the total price is : £{:.2f}".format(
        cart.getTotal()))
