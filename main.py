from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True

while is_on:
    option = menu.get_items()
    user_action = input(f"What would you like?({option}): ")
    if user_action == 'off':
        is_on = False
    elif user_action == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_action)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
