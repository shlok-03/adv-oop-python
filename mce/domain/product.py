from .money import Money
from .shipping import ShippingCalculator

class Product:
    
    def __init__(self, product_id: str, name: str, price: Money):
        self._id = product_id
        self._name = name
        if not isinstance(price, Money):
            raise ValueError("Price needs to be of type Money")
        self._price = price
         
        
    @property
    def id(self):
        return self._id
    

    
    def get_total_price(self):
        return self._price
    

    
    def __str__(self):
        return f"{self._name}\nPrice:\n---Base: {self.get_total_price()}\n---Tax: {self.calculate_tax()}"
    

    def to_dict(self):
        return {
            "id": self._id,
            "name": self._name,
            "price": self._price.to_dict()
        }    

    @staticmethod
    def from_dict(data):
        return Product(data["id"], data["name"], Money.from_dict(data["price"]))
    
class PhysicalProduct(Product):
    
    def __init__(self, product_id: str, name: str, price: Money, shipping_calculator: ShippingCalculator):
        super().__init__(product_id, name, price)
        self._shipping_calculator = shipping_calculator
        
    
    def get_total_price(self):
        return self._price + self._shipping_calculator.calculate()
    
    

class DigitalProduct(Product):
    pass



class SubscriptionProduct(Product):
    def __init__(self, product_id, name, price, months: int):
        super().__init__(product_id, name, price)
        self._months = months
        
    def get_total_price(self):
        return self._price * self._months




class FreeProduct(Product):
    def get_total_price(self):
        return Money(0, "USD")
    
    
class LimitedQuantityProduct(Product):
    pass
