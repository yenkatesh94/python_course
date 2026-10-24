"""Encapsulation groups data and methods together and controls how data is accessed.
This example uses a bank account to discuss why public attributes can be changed directly.
"""

class Bank:
    def __init__(self):
        self.balance = 1000

    def show_balance(self):
        print(self.balance)

    def deposit(self, amount):
        self.balance += amount

b = Bank()

b.balance = 0
b.show_balance()
# Topic 19: Encapsulation