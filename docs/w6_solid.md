# SOLID Principles

SOLID is an acronym for five design principles that help make software more maintainable, scalable, and flexible.

## **S** - Single Responsibility Principle (SRP)

A class should have **only one reason to change**, meaning it should have only one responsibility or job.

**Benefits**: Easier to understand, test, and modify
```python
# Bad: Class has multiple responsibilities
class User:
    def save_to_database(self): pass
    def send_email_notification(self): pass
    def generate_report(self): pass

# Good: Each class has one responsibility
class User:
    def save_to_database(self): pass

class EmailNotifier:
    def send_notification(self, user): pass

class ReportGenerator:
    def generate_report(self, user): pass
```

---

## **O** - Open/Closed Principle (OCP)

Software entities should be **open for extension** but **closed for modification**.

**Benefits**: Add new features without changing existing code
```python
# Bad: Must modify the Processor class to add new payment methods
class PaymentProcessor:
    def process(self, method):
        if method == "credit_card": ...
        elif method == "paypal": ...
        elif method == "bitcoin": ...  # Need to modify!

# Good: Extend with new strategies without modifying existing code
class PaymentStrategy(ABC):
    @abstractmethod
    def process(self): pass

class CreditCardProcessor(PaymentStrategy):
    def process(self): pass

class PayPalProcessor(PaymentStrategy):
    def process(self): pass
```

---

## **L** - Liskov Substitution Principle (LSP)

Derived classes should be **substitutable for their base classes** without breaking functionality.

**Benefits**: Polymorphism works correctly; subtypes are reliably interchangeable
```python
# Bad: Bird subclasses violate expectations
class Bird:
    def fly(self): pass

class Penguin(Bird):
    def fly(self): 
        raise NotImplementedError("Penguins can't fly!")

# Good: Classes respect the contract
class Bird:
    def move(self): pass

class FlyingBird(Bird):
    def move(self): self.fly()

class Penguin(Bird):
    def move(self): self.swim()
```

---

## **I** - Interface Segregation Principle (ISP)

Clients should not be forced to depend on interfaces they don't use.

**Benefits**: Smaller, more focused interfaces; reduced dependencies
```python
# Bad: Force classes to implement unused methods
class Worker(ABC):
    @abstractmethod
    def work(self): pass
    @abstractmethod
    def eat_lunch(self): pass

class Robot(Worker):
    def work(self): pass
    def eat_lunch(self): pass  # Robots don't eat!

# Good: Segregate into focused interfaces
class Workable(ABC):
    @abstractmethod
    def work(self): pass

class Eatable(ABC):
    @abstractmethod
    def eat_lunch(self): pass

class Robot(Workable):
    def work(self): pass

class Human(Workable, Eatable):
    def work(self): pass
    def eat_lunch(self): pass
```

---

## **D** - Dependency Inversion Principle (DIP)

High-level modules should depend on **abstractions**, not on **concrete implementations**.

**Benefits**: Loose coupling; easier to test and swap implementations
```python
# Bad: High-level code depends on concrete classes
class Order:
    def __init__(self):
        self.database = MySQLDatabase()  # Tightly coupled!
    
    def save(self):
        self.database.save(self)

# Good: Depend on abstractions
class Database(ABC):
    @abstractmethod
    def save(self, data): pass

class Order:
    def __init__(self, database: Database):
        self.database = database  # Flexible!
    
    def save(self):
        self.database.save(self)
```

---

## Quick Reference Table

| Principle | Focus | Key Idea |
|-----------|-------|----------|
| **SRP** | Class Responsibility | One reason to change |
| **OCP** | Extension vs Modification | Extend, don't modify |
| **LSP** | Substitutability | Subtypes must honor contracts |
| **ISP** | Interface Design | Don't force unused dependencies |
| **DIP** | Dependency Direction | Depend on abstractions |

---

