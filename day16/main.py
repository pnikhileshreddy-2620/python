from Menu import Menu
from CoffeeMaker import CoffeeMaker
from MoneyMachine import MoneyMachine

Money_machine =MoneyMachine()
print(Money_machine.report())
menu =Menu()
cm =CoffeeMaker()
print(cm.report())
print(menu.get_items())
print(menu.find_drink('latte'))