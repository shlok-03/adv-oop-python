# Abstract Classes in Python

## Definition

An **abstract class** is a class that cannot be instantiated directly and serves as a template for subclasses. It defines a set of methods that subclasses **must implement**. Abstract classes enforce a contract that derived classes must follow.

### Key Characteristics:
- Cannot be instantiated (you can't create an instance of the abstract class itself)
- Contains one or more abstract methods
- Subclasses must implement all abstract methods
- Can contain both abstract and concrete methods
- Enforces consistency across implementations

### When to Use:
- Creating a template/interface that multiple classes must follow
- Defining a common behavior contract for subclasses
- Preventing incomplete implementations
- Establishing a clear inheritance hierarchy

---

## Syntax

### Basic Structure

```python
from abc import ABC, abstractmethod

# Step 1: Inherit from ABC (Abstract Base Class)
class MyAbstractClass(ABC):
    
    # Step 2: Use @abstractmethod decorator
    @abstractmethod
    def required_method(self):
        pass
    
    # Can also have concrete methods
    def concrete_method(self):
        return "This is implemented"
```



## Abstract Methods with Properties

Abstract classes can also enforce abstract properties:

```python
from abc import ABC, abstractmethod

class DataStore(ABC):
    
    @property
    @abstractmethod
    def name(self) -> str:
        """Name of the data store (must be implemented)"""
        pass
    
    @abstractmethod
    def save(self, data: dict) -> bool:
        pass


class DatabaseStore(DataStore):
    
    @property
    def name(self) -> str:
        return "MySQL Database"
    
    def save(self, data: dict) -> bool:
        print(f"Saving to {self.name}: {data}")
        return True


# Usage
store = DatabaseStore()
print(store.name)  # "MySQL Database"
store.save({"id": 1, "name": "John"})
```

---

## Why Use Abstract Classes?

### 1. **Prevents Incomplete Implementations**

**Without Abstract Class**:
```python
class PaymentProcessor:
    def process_payment(self, amount):
        raise NotImplementedError("Subclass must implement this")

# This works—no error!
processor = PaymentProcessor()

# Error only happens later when you try to use it
processor.process_payment(100)  # Crashes at runtime
```

**With Abstract Class**:
```python
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

# Error caught immediately!
processor = PaymentProcessor()  
# TypeError: Can't instantiate abstract class PaymentProcessor
```

### 2. **Enforces Interface Implementation**

**Without Abstract Class**:
```python
class PaymentProcessor:
    def process_payment(self):
        raise NotImplementedError()

class CreditCardProcessor(PaymentProcessor):
    pass  # Forgot to implement process_payment!

# No error—but the class is incomplete
cc = CreditCardProcessor()
cc.process_payment()  # Crashes when called
```

**With Abstract Class**:
```python
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self):
        pass

class CreditCardProcessor(PaymentProcessor):
    pass  # Error immediately!

#TypeError: Can't instantiate abstract class CreditCardProcessor
# with abstract methods process_payment
```

### 3. **Clear Contract and Documentation**

The abstract class clearly documents what subclasses must do:

```python
class ShippingCalculator(ABC):
    """All shipping methods MUST implement these methods"""
    
    @abstractmethod
    def calculate(self, weight, distance) -> float:
        """Return the shipping cost"""
        pass
    
    @abstractmethod
    def get_delivery_time(self) -> str:
        """Return estimated delivery time"""
        pass
    # This is a clear contract!
```

### 4. **Better IDE Support**

IDEs can provide:
- Automatic method stub generation when creating subclasses
- Warnings if you forget to implement required methods
- Better code completion and navigation

### 5. **Runtime Safety**

Abstract classes guarantee that all critical methods are implemented:

```python
def process_order(shipping: ShippingCalculator):
    # You know calculate() MUST be implemented
    cost = shipping.calculate(weight, distance)  # Never fails
    return cost
```

### 6. **Cleaner Client Code**

No need for defensive programming:

```python
# With regular classes—need error handling
try:
    cost = shipping.calculate(10, 100)
except NotImplementedError:
    print("Implementation missing!")

# With abstract classes—guaranteed to work
cost = shipping.calculate(10, 100)  # Always safe
```

### 7. **Improved Code Clarity**

Abstract classes clearly signal intent:
- "This is meant to be subclassed" ✓
- "Every subclass MUST implement these methods" ✓
- "This code establishes a pattern" ✓

---



## Best Practices

1. **Use abstract classes for defining contracts** - Not as a way to add common code
2. **Keep abstract methods focused** - Each method should represent one responsibility
3. **Implement common logic in concrete methods** - Not all methods need to be abstract
4. **Use descriptive docstrings** - Explain what subclasses must do
5. **Avoid deep inheritance hierarchies** - Keep it simple and maintainable

---


**Bottom Line**: Use abstract classes when you want to define a contract that subclasses must follow. It's a best practice for creating robust, maintainable code.
