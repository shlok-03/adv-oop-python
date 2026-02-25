from .money import Money

class Product:
    
    def __init__(self, product_id: str, name: str, price: Money):
        self._id = product_id
        self._name = name
        if not isinstance(price, Money):
            raise ValueError("Price needs to be of type Money")
        self._price = price
        
    @property
    def price(self):
        return self._price
    
    
    def __str__(self):
        return f"Name: {self._name}; Price: {self.price}"