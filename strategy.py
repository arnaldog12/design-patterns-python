from abc import abstractmethod


class ShoppingCart:
    def __init__(self, list_items):
        self.list_items = list_items

    def pay(self, payment_strategy):
        payment_strategy.pay()


# Strategy Pattern
class PaymentStrategy:
    @abstractmethod
    def pay(self):
        pass


class CreditCart(PaymentStrategy):
    def __init__(self, name, card_number, cvv, exp_date):
        self.name = name
        self.card_number = card_number
        self.cvv = cvv
        self.exp_date = exp_date

    def pay(self):
        print(f"paying with credit card nº: {self.card_number}")


class PayPal(PaymentStrategy):
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def pay(self):
        print(f"paying with paypal from user: {self.email}")


cart = ShoppingCart(["item 1", "item 2", "item 3"])
cart.pay(CreditCart("Arnaldo", "1111.2222.3333.4444", "000", "2100/01/01"))
cart.pay(PayPal("arnaldo@email.com", "1234"))
