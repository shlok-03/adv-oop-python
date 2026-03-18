from .notifier import Notifier
from ..domain.order import Order


class EmailNotifier(Notifier):
    
    def send(self, order: Order):
        print("Sending email notification")