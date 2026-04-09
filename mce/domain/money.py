from decimal import Decimal


class Money:
    
    def __init__(self, amount: Decimal, currency: str):
        self._amount = amount
        self._currency = currency
        
    @property
    def currency(self):
        return self._currency

    
    def __mul__(self, multiplier: Decimal):
        return Money(self._amount * multiplier, self._currency)
    
    def __add__(self, other):
        if self._currency != other.currency:
            raise ValueError("Currency mismatch")
        return Money(self._amount + other.amount, self.currency)

    @property
    def amount(self):
        return self._amount
    
    def __str__(self):
        return f"{self.amount:.2f} {self.currency}"
    
    
    def to_dict(self):
        return {
            "amount": str(self.amount),
            "currency": self.currency
        }
        
    
    @staticmethod
    def from_dict(data):
        return Money(Decimal(data["amount"]), data["currency"])