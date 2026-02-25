from .customer import Customer
from .product import Product
from .orderline import OrderLine
from .money import Money

class Order:
    def __init__(self, order_id: str, customer: Customer, order_line: OrderLine):
        self._id = order_id
        self._customer = customer
        
        self._lines = [order_line]
        
        
    def  add_product(self, product: Product, quantity: int):
        self._lines.append(OrderLine(product, quantity))
        
    def total(self) -> Money:
        return sum(line.line_total() for line in self._lines)
    

    
    @property
    def lines(self):
        return list(self._lines)
    
    def __str__(self):
        ret_val = "Order: \n"
        for line in self._lines:
            ret_val +=  line
            ret_val += "\n"
        return ret_val