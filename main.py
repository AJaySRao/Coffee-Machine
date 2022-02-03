
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
#

coffee = CoffeeMaker()
m = Menu()
money = MoneyMachine()


def process():
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == 'off':
        print("Machine is shutting down...")
        exit()
    elif choice == 'report':
        coffee.report()
        money.report()
    else:
        if choice in m.get_items():
            order = m.find_drink(choice)
            c = order.cost
            if coffee.is_resource_sufficient(order):
                if money.make_payment(c):
                    coffee.make_coffee(order)

    process()

process()
