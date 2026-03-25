from ..domain.order import Order 
from .repository import Repository

class JSONRepository(Repository):
    def save(self, order: Order):
        print("Save to file")
        #  with open("order.json", "w") as f:
        #     f.write(...)