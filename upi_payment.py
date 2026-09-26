from payment_strategy import PaymentStrategy

class UPIPayment(PaymentStrategy):
    def process_payment(self, amount):
        print(f"Processing UPI payment for amount: ${amount}")