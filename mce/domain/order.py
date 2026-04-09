from .customer import Customer
from .product import Product
from .orderline import OrderLine
from .money import Money
from typing import List

class Order:
    def __init__(self, order_id: str, customer: Customer):
        self._id = order_id
        self._customer = customer
        
        self._lines: List[OrderLine] = []
        
        
    def validate(self):
        pass
        
    def  add_product(self, product: Product, quantity: int):
        self._lines.append(OrderLine(product, quantity))
        
    def total(self) -> Money:
        sum = Money(0, "USD")
        for line in self._lines:
            sum += line.line_total()
            
        return sum
    
    
    
    @property
    def customer(self):
        return self._customer
    
    @property
    def lines(self):
        return list(self._lines)
    
    @property
    def id(self):
        return self._id
    
    def __str__(self):
        ret_val = "Order: \n"
        for line in self._lines:
            ret_val +=  str(line)
            ret_val += "\n"
        return ret_val


    

    def to_dict(self):
        # order_lines_dict = []
        
        # for line in self._lines:
        #     order_lines_dict.append(  {
        #             "product_id": line.product.id,
        #             "quantity": line.quantity
        #         })
        
        return {
            "id": self._id,
            "customer": self._customer.to_dict(),
            "lines": [
                line.to_dict()
                for line in self._lines
            ]
        }
    
    @staticmethod
    def from_dict(data):
        order = Order(data["id"], Customer.from_dict(data["customer"]))
        for line_dict in data["lines"]:
            order_line = OrderLine.from_dict(line_dict)
            order.add_product(order_line.product, order_line.quantity)
        
        return order
        