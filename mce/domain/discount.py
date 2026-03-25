from abc import ABC, abstractmethod
from .order import Order
from .money import Money

class DiscountStrategy(ABC):    
    @abstractmethod   
    def calculate(self, order: Order) -> Money:
        pass


class PercentageDiscount(DiscountStrategy):
    def calculate(self, order):
        return order.total() * 0.1

class FixedDiscount(DiscountStrategy):
    def calculate(self, order):
        return Money(20, "USD")

class LoyaltyDiscount(DiscountStrategy):
    def calculate(self, order):
        if order.customer.is_loyal:
            return order.total() * 0.15
        return Money(0, "USD")
    

class CompositeDiscount(DiscountStrategy):
    
    def __init__(self, strategies):
        self._strategies = strategies
        
    def calculate(self, order):
        discount = Money(0, "USD")
        for strategy in self._strategies:
            discount += strategy.calculate(order)
        return discount