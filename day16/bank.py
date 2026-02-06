class Bank:
    def __init__(self,name,accountNumber,balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance
    def display(self):
        return f"My name is {self.name} and account number {self.accountNumber} and balance {self.balance}"
    def deposit(self,amount):
        if amount>=1:
            # self.accountNumber=account_number
            self.balance +=amount
        else:
            print("Please enter the greater than 1")
    def withdraw(self,amount):
        if self.balance < amount:
            print("Insufficient fund")
        else:
            self.balance -=amount

cust1 = Bank('dell',1234,1000)
cust1.deposit(1)
print(cust1.display())
cust1.withdraw(100)
print(cust1.display()
      )