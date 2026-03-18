from ..domain.order import Order


class Notifier:
    def send(self, order: Order):
        raise NotImplementedError
