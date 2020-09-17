
class BankAccount:
    def __init__(self, int_rate = 0, balance=0):
        self.int_rate = int_rate
        self.balance = balance  
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate = 0.02, balance = 0)

    def deposit(self, amount):
        self.account.balance += amount
        
        return self

    def withdraw(self, amount):
        if self.account.balance < amount:
            print("Insufficient Funds: Charging a $5 fee")
            fee = 5
            self.account.balance -= fee
        else:
            self.account.balance -= amount
        return self

    def display_user_balance(self):
        print(f"User:  {self.name}, Balance:  ${self.account.balance}")	

    def yield_interest(self):
        if self.account.balance > 0:
            self.account.balance = self.account.balance + self.account.balance * self.int_rate
        return self
       
    def transfer_money(self, other_user, amount):
        other_user.deposit(amount)
        self.withdraw(amount) 
        return self 

guido = User("Guido van Rossum", "guido@python.com")    #instance 1
monty = User("Monty Python", "monty@python.com")        #instance 2
laura = User("Laura Bullock", "laura@python.com")       #instance 3

account1 = BankAccount(.01, 200)    
account2 = BankAccount(.01, -3)


print("*"*20 + "USER 1" + "*"*20)

guido.deposit(150).deposit(200).deposit(200).withdraw(500).display_user_balance()
print("*"*46)
