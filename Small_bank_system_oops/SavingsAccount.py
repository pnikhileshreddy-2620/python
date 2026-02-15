from python.Small_bank_system_oops.BankAccount import BankAccount


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, account_number, balance,interest_rate):
        super().__init__(account_holder, account_number, balance)
        self.interest_rate =interest_rate
    def add_interest(self):
        balance =self.balance*self.interest_rate/100
        self.balance +=balance
        print(f"New Balance after interest {self.balance}")
