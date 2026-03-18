from ..infrastructure.repository import Repository
from ..domain.payment import PaymentProcessor
from ..domain.order import Order
from ..infrastructure.notifier import Notifier



"""
Validate Order

Process payment

Save order

Send notification

"""

class CheckoutService:
    
    def __init__(self, repository: Repository, payment_processor: PaymentProcessor, notifier: Notifier):
        self._repo = repository
        self._payment = payment_processor
        self._notifier = notifier
        
    def checkout(self, order: Order):
        
        order.validate()
        
        total = order.total()
        self._payment.process(total)
        
        self._repo.save(order)
        
        self._notifier.send(order)