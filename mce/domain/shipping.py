from .money import Money
from abc import ABC, abstractmethod

class ShippingCalculator(ABC):
    
    @abstractmethod
    def calculate(self) -> Money:
        pass
    
    
class StandardShipping(ShippingCalculator):
    
    def calculate(self):
        return Money(10, 'USD')
    

class HeavyShipping(ShippingCalculator):
    
    def calculate(self):
        return Money(25, 'USD')
    
    
class InternationalShipping(ShippingCalculator):
    
    def calculate(self):
        return Money(50, 'USD')


class FreeShipping(ShippingCalculator):
    
    def calculate(self):
        return Money(0, 'USD')
    

class WeightDependentShipping(ShippingCalculator):
    
    def __init__(self, weight: float):
        super().__init__()
        self._weight = weight
        
    def calculate(self):
        return Money(self._weight * 2, 'USD')
    

class PromotionalShipping(ShippingCalculator):
    
    def __init__(self, discount):
        super().__init__()
        self._discount = discount
        
    def calculate(self):
        return Money(max(0, 10 - self._discount), 'USD')
        