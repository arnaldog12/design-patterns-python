from abc import abstractmethod


# Component Pattern
class MenuComponent:
    @abstractmethod
    def add(self, menu_component):
        pass

    @abstractmethod
    def print(self):
        pass


class MenuItem(MenuComponent):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def print(self):
        print(f"    {self.name}: {self.price}")


# Client
class Menu(MenuComponent):
    def __init__(self, name):
        self.name = name
        self.list_items = []

    def add(self, menu_component):
        return self.list_items.append(menu_component)

    def print(self):
        print(f"[{self.name}]")
        print("-" * 15)
        for item in self.list_items:
            item.print()
        print()


menu_lunch = Menu("Lunch Menu")
menu_lunch.add(MenuItem("rice and beans", 10.0))
menu_lunch.add(MenuItem("oranje juice", 5.0))

menu_dinner = Menu("Dinner Menu")
menu_dinner.add(MenuItem("pizza", 40.0))
menu_dinner.add(MenuItem("soda", 8.0))

all_menus = Menu("All Menus")
all_menus.add(menu_lunch)
all_menus.add(menu_dinner)

all_menus.print()

print("xxxxxxxxxxxxx")
menu_dinner.add(menu_lunch)
menu_dinner.print()
