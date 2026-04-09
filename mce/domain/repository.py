from abc import abstractmethod, ABC
from typing import Dict
from .order import Order

class PersistanceRepository(ABC):
    @abstractmethod
    def save(self, obj):
        pass
    
    
    @abstractmethod
    def load(self):
        pass



class Repository(ABC):
    
    @abstractmethod
    def add(self, obj):
        pass
    
    
    @abstractmethod
    def get(self):
        pass
    



class OrderRepository(Repository):
    
    def __init__(self, repository: PersistanceRepository):
        self._repository = repository
        self._orders = {}
        self._load()
        

    def add(self, order: Order):
        self._orders[order.id] = order
        self._save()
        
    def get(self, id: str) -> Order:
        self._orders.get(id)
        
    def _load(self):
        data = self._repository.load()
        if not data is None:
            for obj_dict in data:
                self.add(Order.from_dict(obj_dict))
            
    def _save(self):
        self._repository.save([order.to_dict() for order in  self._orders.values()])
        
    
    
    
