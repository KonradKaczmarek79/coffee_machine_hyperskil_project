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
