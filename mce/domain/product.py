from .money import Money

class Product:
    
    def __init__(self, product_id: str, name: str, price: Money):
        self._id = product_id
        self._name = name
        if not isinstance(price, Money):
            raise ValueError("Price needs to be of type Money")
        self._price = price
        
    
    def get_total_price(self):
        return self._price
    
    def calculate_tax(self):
        return Money(0, "USD")
    
    
    def __str__(self):
        return f"{self._name}\nPrice:\n---Base: {self.get_total_price()}\n---Tax: {self.calculate_tax()}"
    
    

class PhysicalProduct(Product):
    
    def __init__(self, product_id: str, name: str, price: Money, shipping_cost: Money):
        super().__init__(product_id, name, price)
        self._shipping_cost = shipping_cost
        
    
    def get_total_price(self):
        return self._price + self._shipping_cost
    
    def calculate_tax(self):
        return self._price * 0.15
    

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