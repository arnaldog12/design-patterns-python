from abc import abstractmethod


class Beverage:
    def __init__(self, description="Unknown Beverage"):
        self.description = description

    @abstractmethod
    def cost(self):
        return 0.0


class Espresso(Beverage):
    def __init__(self) -> None:
        super().__init__("Espresso Coffee")

    def cost(self):
        return 0.5


class Capuccino(Beverage):
    def __init__(self) -> None:
        super().__init__("Capuccino Coffee")

    def cost(self):
        return 1.0


class CondimentDecorator(Beverage):
    @abstractmethod
    def cost(self):
        return 0.0


class Milk(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage
        self.description = self.beverage.description + " + Milk"

    def cost(self):
        return 0.1 + self.beverage.cost()


class Whip(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage
        self.description = self.beverage.description + " + Whip"

    def cost(self):
        return 0.25 + self.beverage.cost()


beverage = Espresso()
print(f"{beverage.description}: {beverage.cost():.2f}")

beverage_2 = Capuccino()
beverage_2 = Milk(beverage_2)
beverage_2 = Milk(beverage_2)
beverage_2 = Whip(beverage_2)
print(f"{beverage_2.description}: {beverage_2.cost():.2f}")
