def print_blanks(func):
    def wrapper(*args, **kwargs):
        print()
        func(*args, **kwargs)
        print()
    return wrapper



class CoffeeMachine:
    """The creation of the CoffeeMachine object and the related functionality."""

    coffee_attributes = {
        "1": {"kind": "espresso", "water": 250, "beans": 16, "milk": 0, "cups": 1, "money": 4},
        "2": {"kind": "latte", "water": 350, "beans": 20, "milk": 75, "cups": 1, "money": 7},
        "3": {"kind": "cappuccino", "water": 200, "beans": 12, "milk": 100, "cups": 1, "money": 6},
    }

    def __init__(self, water, milk, coffee_beans, disposable_cups, money):
        """The initializer for the CoffeeMachine class.

        :param water: a integer representing the amount of water in the coffee machine.
        :param milk: a integer representing the amount of milk in the coffee machine.
        :param coffee_beans: a integer representing the amount of coffee beans in the coffee machine.
        :param disposable_cups: a integer representing the amount of disposable cups in the coffee machine.
        :param money: a int representing the amount of money the coffee machine has to pay.
        """
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.disposable_cups = disposable_cups
        self.money = money

    def __repr__(self):
        return f"Coffee Machine({self.water}, {self.milk}, {self.coffee_beans}, {self.disposable_cups}, {self.money})"

    def __str__(self):
        return (f"\nThe coffee machine has:\n"
                f"{self.water} ml of water\n"
                f"{self.milk} ml of milk\n"
                f"{self.coffee_beans} g of coffee beans\n"
                f"{self.disposable_cups} disposable cups\n"
                f"${self.money} of money\n")

    def __buy_espresso(self):
        """Changes the values for each supply according to the ones needed to prepare espresso."""
        espresso_params = self.coffee_attributes["1"]

        self.money += espresso_params["money"]
        self.water -= espresso_params["water"]
        self.coffee_beans -= espresso_params["beans"]
        self.disposable_cups -= espresso_params["cups"]

    def __buy_latte(self):
        """Changes the values for each supply according to the ones needed to prepare latte."""
        latte_params = self.coffee_attributes["2"]

        self.money += latte_params["money"]
        self.water -= latte_params["water"]
        self.milk -= latte_params["milk"]
        self.coffee_beans -= latte_params["beans"]
        self.disposable_cups -= latte_params["cups"]

    def __buy_cappuccino(self):
        """Changes the values for each supply according to the ones needed to prepare cappuccino."""
        cappuccino_params = self.coffee_attributes["3"]

        self.money += cappuccino_params["money"]
        self.water -= cappuccino_params["water"]
        self.milk -= cappuccino_params["milk"]
        self.coffee_beans -= cappuccino_params["beans"]
        self.disposable_cups -= cappuccino_params["cups"]

    def check_machine_capacity(self, coffee_shortcut="1"):
        if self.coffee_attributes[coffee_shortcut].get("water", 0) > self.water:
            print("Sorry, not enough water!")
            return False
        elif self.coffee_attributes[coffee_shortcut].get("milk", 0) > self.milk:
            print("Sorry, not enough milk!")
            return False
        elif self.coffee_attributes[coffee_shortcut].get("beans", 0) > self.coffee_beans:
            print("Sorry, not enough coffee beans!")
            return False
        elif self.coffee_attributes[coffee_shortcut].get("cups", 0) > self.disposable_cups:
            print("Sorry, not enough disposable cups!")
            return False
        else:
            print("I have enough resources, making you a coffee!")
            return True

    def buy_cup_of_coffee(self, kind_of_coffee):

        if kind_of_coffee == "back" or kind_of_coffee not in self.coffee_attributes.keys():
            return

        capacity = self.check_machine_capacity(coffee_shortcut=kind_of_coffee)

        if not capacity:
            return
        if kind_of_coffee == "1":
            self.__buy_espresso()
        elif kind_of_coffee == "2":
            self.__buy_latte()
        elif kind_of_coffee == "3":
            self.__buy_cappuccino()

    def fill_supplies(self, key, value):
        """Add specified quantity of supplies to the coffee machine.

        :param key: possible values of a key ['water', 'milk', 'coffee_beans', 'disposable_cups', 'money']
        :param value: how many supply you want to add
        :return:
        """
        if key in self.__dict__ and key != 'money':
            self.__dict__[key] += value

    def take_money(self):
        money = self.money
        self.money = 0
        return money


    def fill_each_supply(self):
        message_prefix = "Write how many "
        message_suffix = " you want to add:\n"
        units = ("ml of ", "ml of ", "grams of ", "")
        supplies = ("water", "milk", "coffee_beans", "disposable_cups")
        for supply, unit in zip(supplies, units):
            quantity = int(input(f"{message_prefix}{unit}{supply.replace('_', ' ')}{message_suffix}"))
            self.fill_supplies(supply, quantity)


    def perform_action(self):
        action = input("Write action (buy, fill, take, remaining, exit):\n")
        if action == "buy":
            print()
            kind_of_coffee = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: \n")
            self.buy_cup_of_coffee(kind_of_coffee)
            print()
        elif action == "fill":
            print()
            self.fill_each_supply()
            print()
        elif action == "take":
            money = self.take_money()
            print(f"\nI gave you ${money}\n")
        elif action == "remaining":
            print(self)
        return action


def main():

    coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)
    worker = "run"

    while worker != "exit":
        worker = coffee_machine.perform_action()


if __name__ == '__main__':
    main()
