from ..domain.repository import PersistanceRepository


class InMemoryRepository(PersistanceRepository):
    def save(self, obj):
        print("Saving to memory")
    
    def load(self):
        print("Loading from memory")