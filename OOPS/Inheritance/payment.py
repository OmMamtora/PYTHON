# Create a Payment class with attributes amount and method. Subclass it into 
# CreditCardPayment and PayPalPayment, adding specific attributes like card_number for the
# former and email for the latter.


class Payment:
    def __init__(self, amount, method):
        self.amount = amount
        self.method = method

    def display_info(self):
        print(f"Amount: ${self.amount}, Payment Method: {self.method}")

class CreditCardPayment(Payment):
    def __init__(self, amount, card_number):
        super().__init__(amount, "Credit Card")
        self.card_number = card_number

    def display_info(self):
        super().display_info()
        print(f"Card Number: {self.card_number}")

class PayPalPayment(Payment):
    def __init__(self, amount, email):
        super().__init__(amount, "PayPal")
        self.email = email

    def display_info(self):
        super().display_info()
        print(f"PayPal Email: {self.email}")

credit_card_payment = CreditCardPayment(100, "1234-5678-9876-5432")
credit_card_payment.display_info()

print("\n")

paypal_payment = PayPalPayment(50, "om@gmail.com")
paypal_payment.display_info()
