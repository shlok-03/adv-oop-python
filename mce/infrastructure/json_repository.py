from ..domain.order import Order 
from .repository import Repository

class JSONRepository(Repository):
    def save(self, order: Order):
         with open("order.json", "w") as f:
            f.write(...)