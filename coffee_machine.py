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
