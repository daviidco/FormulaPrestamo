import decimal


class Credit:
    def __init__(self, credit_value, num_payments, interest):
        self.credit_value = credit_value
        self.num_payments = num_payments
        self.interest = decimal.Decimal(interest)

        term1 = decimal.Decimal((1 + self.interest)) ** self.num_payments
        term2 = (decimal.Decimal(1 + self.interest) ** self.num_payments) - 1
        self.payment = self.credit_value * (self.interest * term1 / term2)
        self.total_payments = self.payment * self.num_payments
        self.financial_cost = self.total_payments - self.credit_value
