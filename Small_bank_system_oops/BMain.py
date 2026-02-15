# Savings Account
from python.Small_bank_system_oops.CheckingAccount import CheckingAccount
from python.Small_bank_system_oops.SavingsAccount import SavingsAccount

savingAccount1 = SavingsAccount("PC", 1, 1000, 5)

savingAccount1.display_balance()
savingAccount1.add_interest()
savingAccount1.deposit(1000)
savingAccount1.withdraw(500)
savingAccount1.display_balance()

# Checking Account
checkingAccount1 = CheckingAccount("Dell", 2, 1000, -250)

checkingAccount1.display_balance()
checkingAccount1.deposit(1000)
checkingAccount1.withdraw(2100)   # allowed
checkingAccount1.withdraw(500)
checkingAccount1.withdraw(5000)  # denied
checkingAccount1.display_balance()
