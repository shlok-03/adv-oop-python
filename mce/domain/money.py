from decimal import Decimal


class Money:
    
    def __init__(self, amount: Decimal, currency: str):
        if amount < 0:
            raise ValueError("Money cannot be negative")
        self._amount = amount
        self._currency = currency
        
    @property
    def currency(self):
        return self._currency

    
    def __mul__(self, multiplier: int):
        return Money(self._amount * multiplier, self._currency)
    
    def __add__(self, other):
        if self._currency != other.currency:
            raise ValueError("Currency mismatch")
        return Money(self._amount + other.amount, self.currency)
    
    @property
    def amount(self):
        return self._amount
    
    def __str__(self):
        return f"{self.amount} {self.currency}"