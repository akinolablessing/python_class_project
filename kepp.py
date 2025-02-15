def test_init(self):
    account_number = '12345'
    initial_balance = 100
    bank = Bank(account_number, initial_balance)
    self.assertEqual(bank.account_number, account_number)
    self.assertEqual(bank.balance, initial_balance)


def test_deposit(self):
    account_number = '12345'
    initial_balance = 100
    bank = Bank(account_number, initial_balance)
    deposit_amount = 50
    self.assertTrue(bank.deposit(deposit_amount))
    self.assertEqual(bank.balance, initial_balance + deposit_amount)


def test_deposit_invalid_amount(self):
    account_number = '12345'
    initial_balance = 100
    bank = Bank(account_number, initial_balance)
    deposit_amount = -50
    self.assertFalse(bank.deposit(deposit_amount))
    self.assertEqual(bank.balance, initial_balance)


def test_withdraw(self):
    account_number = '12345'
    initial_balance = 100
    account = Bank(account_number, initial_balance)
    withdraw_amount = 50
    self.assertTrue(account.withdraw(withdraw_amount))
    self.assertEqual(account.balance, initial_balance - withdraw_amount)


def test_withdraw_insufficient_funds(self):
    account_number = '12345'
    initial_balance = 100
    account = Bank(account_number, initial_balance)
    withdraw_amount = 150
    self.assertFalse(account.withdraw(withdraw_amount))
    self.assertEqual(account.balance, initial_balance)


def test_get_balance(self):
    account_number = '12345'
    initial_balance = 100
    account = Bank(account_number, initial_balance)
    self.assertEqual(account.get_balance(), initial_balance)
