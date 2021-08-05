from abc import abstractmethod


class MealTemplate:
    def __init__(self, name):
        self.name = name

    def go(self):
        self.prepare()
        self.cook()
        self.eat()

    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def cook(self):
        pass

    @abstractmethod
    def eat(self):
        pass


class Pizza(MealTemplate):
    def __init__(self, name, ingredient):
        super().__init__(name)
        self.ingredient = ingredient

    def prepare(self):
        print(f"preparing {self.name}...")
        print(f"adding {self.ingredient}")

    def cook(self):
        print(f"cooking {self.name}...")

    def eat(self):
        print(f"eating {self.name}...")


class Tea(MealTemplate):
    def __init__(self, name, temperature):
        super().__init__(name)
        self.temperature = temperature

    def prepare(self):
        print(f"preparing {self.name}...")

    def cook(self):
        print(f"cooking {self.name} under {self.temperature}ºC...")

    def eat(self):
        print(f"drinking {self.name}...")


pizza = Pizza("my pizza", "cheese")
pizza.go()
print()

tea = Tea("black tea", 80)
tea.go()
