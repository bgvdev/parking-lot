from payment_strategy import PaymentStrategy

class CardPayment(PaymentStrategy):
    def process_payment(self, amount):
        print(f"Processing credit card payment for amount: ${amount}")