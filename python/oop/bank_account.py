class BankAccount:
    def __init__(self, int_rate =0.01, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.amount = amount
        self.balance = self.amount + self.balance
        return self
    def withdraw(self, amount):
        self.balance = self.balance - self.amount
        return self
    def display_account_info(self):
        print("Balance: $", self.balance)
        return self
    def yield_interest(self):
        self.balance = self.balance * self.int_rate
        return self

account1 = BankAccount(0,0)

account1.deposit(100).deposit(100).deposit(100).withdraw(50).yield_interest().display_account_info()