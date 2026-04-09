from ..domain.repository import PersistanceRepository
from json import dump, load
import os

class JSONRepository(PersistanceRepository):
    def save(self, obj):
        print("Saving to file")
        with open("orders.json", "w") as f:
            dump(obj, f, indent=2)
            
    
    def load(self):
        print("Loading from file")
        data = None
        if os.path.isfile("orders.json"):
            with open("orders.json", "r") as f:
                data = load(f)
        return data