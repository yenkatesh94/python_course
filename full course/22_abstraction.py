"""Abstraction defines the operations a class must provide while hiding implementation details.
This example uses an abstract ATM interface implemented by different banks.
"""

# Abstraction means:
# - Hiding internal details
# - Showing only what the user needs
# In simple words: User knows what to do, not how it works.

from abc import ABC, abstractmethod


class ATM(ABC):

  @abstractmethod
  def withdraw(self):
    pass


class SBI(ATM):

  def withdraw(self):
    print("Money withdrawn from SBI")


class HDFC(ATM):

  def withdraw(self):
    print("Money withdrawn from HDFC")


atm1 = SBI()
atm1.withdraw()
# Topic 22: Abstraction