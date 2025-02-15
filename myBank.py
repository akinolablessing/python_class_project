from logging import raiseExceptions
from numbers import Number


class Bank:
    def __init__(self):
        self.account_number_and_pin = []
        self.initial_balance = 0
        # self.balance = self.initial_balance

    def user_account_number(self,userAccountNumber):
        if userAccountNumber not in self.account_number_and_pin:
            self.account_number_and_pin.append(userAccountNumber)
            return True
        else:
            return False

    def user_pin(self, userPin):
        if userPin not in self.account_number_and_pin:
          if  len(userPin) == 4:
            self.account_number_and_pin.append(userPin)
            return True
        else:
            return False

    def get_account_number(self):
        return self.account_number_and_pin

    def get_initial_balance(self,initialBalance):
        if initialBalance == self.initial_balance:

            return self.initial_balance
        else:
            raise ValueError

    def deposit_money(self,deposit):
        if deposit > 0:
            self.initial_balance += deposit
            return deposit

        else:
            raise ValueError
    def withdraw_money(self,withdraw):
        if withdraw > 0 and self.initial_balance >= 0:
            self.initial_balance -= withdraw
            return withdraw
        else:
            raise ValueError

    def test_that_get_balance(self):
        return self.initial_balance

