"""Encapsulation groups data and methods together and controls how data is accessed.
This example uses a bank account to discuss why public attributes can be changed directly.
"""

class Bank:

    def __init__(self):
        self.__balance = 1000

    def show_balance(self):
        print("Balance:", self.__balance)

    def deposit(self, amount):
        self.__balance += amount


b = Bank()

b.show_balance()
b.deposit(500)
b.show_balance()
