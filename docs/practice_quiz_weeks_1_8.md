# Advanced OOP with Python  
## Mid-Course Practice Quiz (Weeks 1–8)


## Instructions

- Time: 45–60 minutes  
- Answer all questions  
- Show reasoning for short-answer and design questions  
- Focus on **why**, not just **what**  
- This is a **practice quiz** — use it to identify weak spots  

---
# Part 1 — Core Concepts (Multiple Choice)

### Q1  
What is the primary goal of object-oriented design?

- A. Reduce code size  
- B. Improve performance  
- C. Model systems using objects with responsibility  
- D. Avoid functions  


### Q2  
Which is a **value object**?

- A. Order  
- B. Customer  
- C. Money  
- D. Repository  


### Q3  
Encapsulation ensures:

- A. Variables are hidden  
- B. Code runs faster  
- C. Objects protect their own invariants  
- D. Fewer classes are created  


### Q4  
Single Responsibility Principle means:

- A. One method per class  
- B. One attribute per class  
- C. One reason to change  
- D. One file per class  
 
### Q5  
Polymorphism helps:

- A. Optimize memory  
- B. Replace conditionals based on type  
- C. Improve syntax  
- D. Avoid classes  

### Q6  
Which violates Liskov Substitution Principle?

- A. Overriding a method  
- B. Returning expected type  
- C. Throwing unexpected exceptions  
- D. Adding new methods  

### Q7 
What is wrong with this?

```python
if product.type == "physical":
    # some logic here
```
- A. Syntax error  
- B. Inefficient  
- C. Violates polymorphism  
- D. Too complex  

### Q8  
Why prefer composition over inheritance?

- A. Less code  
- B. Better performance  
- C. More flexibility  
- D. Easier syntax  

### Q9

Which is NOT a valid architecture layer?

- A. Domain  
- B. Application  
- C. Infrastructure  
- D. Database  

### Q10
Correct dependency direction:

- A. Domain → Infrastructure
- B. Infrastructure → Domain
- C. Application → Infrastructure
- D. Domain → UI

## Part 2 — Encapsulation & Responsibility

### Q11

Why is this bad?
```python
 order._lines.append(item)
```

### Q12

Where should validation happen?
```python
if quantity <= 0:
```
Explain which class should handle it and why.

### Q13

What is an anemic domain model?

## Part 3 — Polymorphism & Composition

### Q14

Refactor using polymorphism:

```python
def calculate_price(product):
    if product.type == "digital":
        return product.price
    elif product.type == "physical":
        return product.price + 10
```

### Q15

Why is this design problematic?
```python
class HeavyProduct(Product):
```
### Q16

Give an example where composition is better than inheritance.


## Part 4 — Architecture & Layers

### Q17

Assign each to a layer:

| Component | Layer |
| --- | --- |
| Order | ? |
| CheckoutService | ? |
| JSONRepository | ? |
| CLI interface | ? |

### Q18

Why should domain NOT depend on infrastructure?

### Q19

What is the role of the service layer?

## Part 5 — Dependency Inversion Principle (DIP)

### Q20

What is wrong with this?
```python
class CheckoutService:
    def __init__(self):
        self._repo = JSONRepository()
```

### Q21

Refactor the code in the previous question using DIP.

### Q22

Where should object creation happen?

- A. Domain
- B. Application
- C. Infrastructure
- D. Composition root (main)


## Part 6 — Testing & Reliability

### Q26

What should tests focus on?

- A. Internal variables
- B. Private attributes
- C. Behavior
- D. File structure

### Q27

Why is this a bad test?

```python
assert order._lines == [...]
```

### Q28

What is a mock in testing and why we need it?

### Q29

Why is DIP helpful for testing?

### Q30

Write a pytest test for invalid quantity.

## Part 7 — Error Handling

### Q31

Why use custom exceptions instead of ValueError?

### Q32

Design a simple exception hierarchy for:

- Invalid quantity
- Payment failure

## Part 8 — Design Thinking

### Q33

You need to add a new payment method.

Best approach:

- A. Add if/else
- B. Modify existing class
- C. Add new implementation
- D. Duplicate code

### Q34

You switch from JSON to database.

What should change?

- A. Domain
- B. Application
- C. Repository implementation
- D. Everything

### Q35

Where should this logic live?

| Logic | Class |
| --- | --- |
| applying discounts | ? |
| calculating tax | ? |
| processing payment | ? |

Explain briefly.

## Part 9 — Mini Design Challenge

### Q36

Design a system that supports:

- Multiple discount strategies
- Multiple payment methods
- JSON persistence

Describe:

- Key classes
- Relationships
- Where DIP is applied

## Bonus (Optional)

### Q37

What is the most important design lesson you learned so far?