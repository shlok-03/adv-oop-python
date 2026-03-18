from ..domain.order import Order

class Repository:
    def save(self, oder: Order):
        raise NotImplementedError