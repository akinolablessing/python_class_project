import unittest


from myBank import Bank

class MyTestCase(unittest.TestCase):

   def setUp(self):
    self.bank = Bank()

   def test_that_create_account(self):
       self.assertTrue(self.bank.user_account_number("7047283300"))

   def test_that_craete_pin_should_not_be_more_than_4(self):
       self.assertTrue(self.bank.user_pin("1234"))

   def test_that_initial_money_should_be_zero(self):
       accountPin = "1234"
       self.bank.user_pin(accountPin)
       self.assertEqual(self.bank.get_account_number(),[accountPin])
       self.assertEqual(self.bank.get_initial_balance(0),0)

   def test_that_deposite_money(self):
       accountPin = "1234"
       accountNumber = "7047283300"
       initialBalance = 100
       self.bank.user_pin(accountPin)
       self.bank.user_account_number(accountNumber)
       depositMoney = 50
       self.assertEqual(self.bank.get_account_number(),[accountPin , accountNumber])
       self.assertEqual(self.bank.deposit_money(150),initialBalance + depositMoney)

   def test_that_withdraw_money(self):
       accountPin = "1234"
       accountNumber = "7047283300"
       initialBalance = 150
       self.bank.user_pin(accountPin)
       self.bank.user_account_number(accountNumber)
       withdraw = 50
       self.assertEqual(self.bank.get_account_number(), [accountPin, accountNumber])
       self.assertEqual(self.bank.withdraw_money(100), initialBalance - withdraw)

   def test_that_get_balance(self):
       accountPin = "1234"
       self.bank.user_pin(accountPin)
       self.assertEqual(self.bank.get_account_number(), [accountPin])
       self.assertEqual(self.bank.get_initial_balance(0),0)





