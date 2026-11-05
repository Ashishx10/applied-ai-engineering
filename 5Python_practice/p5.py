# Bank account (classes)
class BankAccount:
    def __init__(self, starting_balance):
        self.balance = starting_balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount} -> balance {self.balance}")
    def withdraw(self, amount):
        if amount > self.balance:
            print(f'"{amount} -> Not enough money", balance still {self.balance}')
        else:
            self.balance -= amount
            print(f"Withdrew: {amount} -> balance {self.balance}")
account = BankAccount(100) 
account.deposit(50)       
account.withdraw(500)     
account.withdraw(40)      
