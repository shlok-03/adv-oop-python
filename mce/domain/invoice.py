from .order import Order

class Invoice:
    
    def __init__(self, order: Order):
        self._order = order
        
    
    def total(self):
        return self._order.total()
    
    def generate_text(self) -> str:
        return str(self._order)
    