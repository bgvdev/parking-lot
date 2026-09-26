from payment_strategy import PaymentStrategy

class Payment:
    PAYMENT_STRATEGY_CASH = 1
    PAYMENT_STRATEGY_CARD = 2

    payment_strategy: PaymentStrategy


    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def process_payment(self, amount):
        if (amount <= 0):
            raise ValueError("Amount must be greater than zero.")
        self.payment_strategy.process_payment(amount)