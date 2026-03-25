# Dependency Inversion Principle (DIP)

## Definition

**High-level modules should not depend on low-level modules. Both should depend on abstractions.**

In other words, depend on **interfaces/abstractions** rather than concrete implementations. This inverts the traditional dependency structure where high-level code depends on low-level details.

### Key Concepts:
- Depend on **abstractions** (abstract classes, interfaces), not concrete implementations
- Use **dependency injection** to provide dependencies
- Decouples code from specific implementations
- Makes testing easier (swap implementations without changing code)
- Promotes flexibility and maintainability

---

## The Problem (Without DIP)

When high-level modules directly depend on low-level concrete classes, you create tight coupling:

```python
# Bad: High-level module depends on concrete implementations
class OrderProcessor:
    def __init__(self):
        self._database = MySQLDatabase()  # Concrete dependency!
        self._email_service = GmailNotifier()  # Concrete dependency!
    
    def process_order(self, order):
        self._database.save(order)  # Tightly coupled
        self._email_service.send_confirmation(order)  # Tightly coupled

# Problems:
# - Hard to test (can't use mock database/email)
# - Must use MySQL and Gmail specifically
# - Changes to MySQLDatabase require changing OrderProcessor
# - Cannot easily swap implementations
```

---

## The Solution (With DIP)

Depend on abstractions. Inject concrete implementations via constructor:

```python
from abc import ABC, abstractmethod

# Step 1: Define abstractions (interfaces)
class Repository(ABC):
    @abstractmethod
    def save(self, order): pass

class Notifier(ABC):
    @abstractmethod
    def send(self, order): pass

# Step 2: Implement concrete classes
class MySQLRepository(Repository):
    def save(self, order):
        # Save to MySQL
        pass

class GmailNotifier(Notifier):
    def send(self, order):
        # Send via Gmail
        pass

# Step 3: High-level module depends on abstractions
class OrderProcessor:
    def __init__(self, repository: Repository, notifier: Notifier):
        self._repo = repository  # Depends on abstraction
        self._notifier = notifier  # Depends on abstraction
    
    def process_order(self, order):
        self._repo.save(order)
        self._notifier.send(order)

# Usage: Inject concrete implementations
db = MySQLRepository()
email = GmailNotifier()
processor = OrderProcessor(db, email)
processor.process_order(my_order)

# Testing: Inject mock implementations
class MockRepository(Repository):
    def save(self, order):
        print(f"Mock saving: {order}")

class MockNotifier(Notifier):
    def send(self, order):
        print(f"Mock sending: {order}")

# Same OrderProcessor works with test implementations!
test_db = FakeRepository()
test_email = FakeNotifier()
test_processor = OrderProcessor(test_db, test_email)
test_processor.process_order(my_order)
```

---

## Example From Our Project

Your `CheckoutService` implements DIP correctly:

```python
# File: mce/application/checkout_service.py

class CheckoutService:
    def __init__(self, 
                 repository: Repository,      # Abstraction, not concrete
                 payment_processor: PaymentProcessor,  # Abstraction
                 notifier: Notifier):        # Abstraction
        self._repo = repository
        self._payment = payment_processor
        self._notifier = notifier
    
    def checkout(self, order: Order):
        order.validate()
        total = order.total()
        self._payment.process(total)
        self._repo.save(order)
        self._notifier.send(order)
```

**Why this is good DIP:**
- `CheckoutService` (high-level) doesn't depend on concrete classes
- It depends on `Repository`, `PaymentProcessor`, `Notifier` (abstractions)
- You can swap `MySQLRepository` with `PostgresRepository` without changing `CheckoutService`
- Easy to test with fake implementations
- Changes to low-level implementations don't cascade up

---

## Benefits

**Loose Coupling**: High-level code doesn't depend on specific low-level implementations  
**Testability**: Inject fake/mock implementations for testing  
**Flexibility**: Swap implementations without changing high-level code  
**Maintainability**: Changes to low-level modules don't cascade upward  
**Reusability**: High-level modules can work with different implementations  

---

## Common Pattern: Dependency Injection

The most common way to apply DIP:

```python
# Constructor Injection (most common)
class Service:
    def __init__(self, dependency: SomeInterface):
        self.dependency = dependency

# Property Injection
class Service:
    dependency: SomeInterface = None

service = Service()
service.dependency = ConcreteDependency()

# Method Injection
class Service:
    def do_work(self, dependency: SomeInterface):
        dependency.do_something()
```

Constructor injection is preferred because it makes dependencies explicit and immutable.
