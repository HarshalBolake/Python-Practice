class Account:
    def __init__(self, account_number,balance):
        self.account_number = account_number
        self.balance = balance
    def deposite(self,amount):
        self.balance += amount
        print(f"{amount} deposited successfully")
    
    def withdraw(self,amount):
        self.balance -= amount
        print(f"{amount} withdraw successfully")

    def display_balance(self):
        print(f"current balance: {self.balance}")

class SavingAccount(Account):
    def add_intrest(self,rate):
        intrest = self.balance * (rate/100)
        self.balance += intrest
        print(f"{intrest} added to your account")

class CurrentAccount(Account):
    def overdraft(self,limit):
        print(f"Overdraft limit: {limit}")

ACC1 = SavingAccount("ACC0001",0)
ACC1.deposite(5000)
ACC1.display_balance()
ACC1.add_intrest(2.5)
ACC1.display_balance()