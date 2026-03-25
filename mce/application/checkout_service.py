from ..infrastructure.repository import Repository
from ..domain.payment import PaymentProcessor
from ..domain.order import Order
from ..infrastructure.notifier import Notifier
from ..domain.discount import DiscountStrategy
from decimal import Decimal

"""
Validate Order

Process payment

Save order

Send notification

"""

class CheckoutService:
    
    def __init__(self, repository: Repository, payment_processor: PaymentProcessor, 
                 notifier: Notifier, discount_calc: DiscountStrategy):
        self._repo = repository
        self._payment = payment_processor
        self._notifier = notifier
        self._discount_calc = discount_calc 
        
    def checkout(self, order: Order):
        
        order.validate()
        
        total = order.total()
        
        # apply tax
        # apply discount
        discount = self._discount_calc.calculate(order) * -1.0
  
        total = total + discount
        
            
        self._payment.process(total)
        
        self._repo.save(order)
        
        self._notifier.send(order)         
                
        