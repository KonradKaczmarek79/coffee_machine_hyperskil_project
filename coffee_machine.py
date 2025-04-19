class CoffeeMachine:
    """The creation of the CoffeeMachine object and the related functionality."""

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
        return (f"The coffee machine has:\n"
                f"{self.water} ml of water\n"
                f"{self.milk} ml of milk\n"
                f"{self.coffee_beans} g of coffee beans\n"
                f"{self.disposable_cups} disposable cups\n"
                f"${self.money} of money")
        
    def __buy_espresso(self):
        """Changes the values for each supply according to the ones needed to prepare espresso."""
        self.money += 4
        self.water -= 250
        self.coffee_beans -= 16
        self.disposable_cups -= 1

    def __buy_latte(self):
        """Changes the values for each supply according to the ones needed to prepare latte."""
        self.money += 7
        self.water -= 350
        self.milk -= 75
        self.coffee_beans -= 20
        self.disposable_cups -= 1

    def __buy_cappuccino(self):
        """Changes the values for each supply according to the ones needed to prepare cappuccino."""
        self.money += 6
        self.water -= 200
        self.milk -= 100
        self.coffee_beans -= 12
        self.disposable_cups -= 1

    def buy_cup_of_coffee(self, kind_of_coffee):
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


def display_coffee_machine_message(coffee_machine: CoffeeMachine):
    print(coffee_machine)
    print()

def fill_each_supply(coffee_machine: CoffeeMachine):
    message_prefix = "Write how many "
    message_suffix = " you want to add:\n"
    units = ("ml of ", "ml of ", "grams of ", "")
    supplies = ("water", "milk", "coffee_beans", "disposable_cups")
    for supply, unit in zip(supplies, units):
        quantity = int(input(f"{message_prefix}{unit}{supply.replace('_', ' ')}{message_suffix}"))
        coffee_machine.fill_supplies(supply, quantity)


def perform_action(coffee_machine: CoffeeMachine):
    action = input("Write action (buy, fill, take):\n")
    if action == "buy":
        kind_of_coffee = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: \n")
        coffee_machine.buy_cup_of_coffee(kind_of_coffee)
    elif action == "fill":
        fill_each_supply(coffee_machine)
    elif action == "take":
        money = coffee_machine.take_money()
        print(f"I gave you ${money}")


def main():

    coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)
    display_coffee_machine_message(coffee_machine)
    perform_action(coffee_machine)
    print()
    display_coffee_machine_message(coffee_machine)


if __name__ == '__main__':
    main()
