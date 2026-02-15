from python.Small_bank_system_oops.BankAccount import BankAccount


class CheckingAccount(BankAccount):
    def __init__(self, account_holder, account_number, balance,overdraft_limit):
        super().__init__(account_holder, account_number, balance)
        self.overdraft_limit=overdraft_limit

    # def withdraw(self,amount):
    #     if self.balance>-amount>self.overdraft_limit:
    #
    #             self.balance -=amount
    #             print(f"New Balance {self.balance}")
    #         else:
    #             print("But do not allow balance to go below overdraft limit")

    def withdraw(self, amount):
        if self.balance - amount >= self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrawal successful. New balance: {self.balance}")
        else:
            print("Withdrawal denied! Overdraft limit exceeded.")