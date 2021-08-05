from abc import abstractmethod


# My Interface
class MyInterface:
    def __init__(self):
        pass

    @abstractmethod
    def get_voltage(self):
        pass


class MySocket(MyInterface):
    def __init__(self, name):
        self.name = name

    def get_voltage(self):
        return 110


# Other Interface (from other library, for example)
class OtherInterface:
    def __init__(self):
        pass

    @abstractmethod
    def get_volts(self):
        pass


class StrangeSocket(OtherInterface):
    def __init__(self, dummy_var):
        self.dummy_var = dummy_var

    def get_volts(self):
        return "220"


# Adapter Pattern
class Adapter(MyInterface):
    def __init__(self, other_interface):
        self.other_interface = other_interface

    def get_voltage(self):
        volts = self.other_interface.get_volts()
        return int(volts)


my = MySocket("My Socket")
print("     MySocket:", my.get_voltage())

other = StrangeSocket("dummy value")
print("StrangeSocket:", other.get_volts())

adapter = Adapter(other)
print("      Adapter:", adapter.get_voltage())
