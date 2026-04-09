
class Customer:
    def __init__(self, customer_id: str, name: str):
        self._id = customer_id
        self._name = name

        
    
    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name    
    
    @property
    def is_loyal(self):
        #todo: add actual logic
        return True

    def to_dict(self):
        return {
            "id": self._id,
            "name": self._name
        }

    @staticmethod
    def from_dict(data):
        return Customer(data["id"], data["name"])

