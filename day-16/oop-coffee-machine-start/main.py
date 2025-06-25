import sys
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cm = CoffeeMaker()
mm = MoneyMachine()
m = Menu()
drink = input("What would you like? (espresso/latte/cappuccino) ")

if drink == 'off':
    print("Coffee machine is off. Goodbye!")
    sys.exit(0)
elif drink == "report":
    cm.report()
    mm.report()
    input("What would you like? (espresso/latte/cappuccino) ")
else:
    drink = m.find_drink(drink)

if cm.is_resource_sufficient(drink):
    if mm.make_payment(drink.cost):
        cm.make_coffee(drink)




