from .product import Product
from .money import Money
from decimal import Decimal


class OrderLine:
    
    def __init__(self, product: Product, quantity: int):
        self._product = product
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")
        self._quantity = quantity
    
    
    
    def line_total(self) -> Money:
        base = self._product.get_total_price() * self._quantity    
        return base
    
    def __str__(self):
        return f"\nProduct: {self._product}\nQuantity: {self._quantity}"
    
    def __repr__(self):
         return f"{self._product} {self._quantity}\n"