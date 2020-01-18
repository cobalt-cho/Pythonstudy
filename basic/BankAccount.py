class BankAccount :
    def __init__(self,balance,name,number):
        self.balance = balance
        self.name = name
        self.number = number

    def withdraw(self,money):
        self.balance-=money
        return self.balance

    def deposit(self,money):
        self.balance+=money
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self,balance,name,number,interest_rate):
        super().__init__(balance,name,number)
        self.interest_rate = interest_rate

    def add_interest(self,interest_rate):
        self.interest_rate = self.balance*interest_rate
        self.balance += self.interest_rate
        return self.balance

class CheckingAccount(BankAccount):
    def __init__(self,balance,name,number,withdraw_charge):
        super().__init__(balance,name,number)
        self.withdraw_charge = withdraw_charge

    def withdraw(self,money):
        return BankAccount.withdraw(self,money + self.withdraw_charge)
