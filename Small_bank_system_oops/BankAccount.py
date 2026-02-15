class BankAccount:
    def __init__(self,account_holder,account_number,balance):
        self.account_holder=account_holder
        self.account_number=account_number
        self.balance=balance

    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
        else:
            print("Invalid Deposit Amount")
            print(f"Balance stay {self.balance}")
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance -=amount
            print(f"Withdrawal successful. New balance: {self.balance}")
        else:
            print("Insufficient funds")
    def display_balance(self):
        print(f"Name {self.account_holder}")
        print(f"Balance {self.balance}")
