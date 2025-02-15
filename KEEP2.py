def deposit(self, amount):
    if amount > 0:
        self.balance += amount
        return True
    return False


def withdraw(self, amount):
    if amount > 0 and self.balance >= amount:
        self.balance -= amount
        return True
    return False


def get_balance(self):
    return self.balance