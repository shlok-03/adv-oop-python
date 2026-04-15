import sys


sys.path.append("C:\\Users\\andre\\dev\\adv-oop-python")

print(sys.path)

from mce.domain.order import Order
from mce.domain.product import Product
from mce.domain.customer import Customer
from mce.domain.money import Money

import pytest


def test_add_item_to_order():
    # Setup
    customer = Customer("1", "John")
    order = Order("1", customer)
    price = Money(25, "USD")
    
    # Execute
    order.add_product(Product("1", "Book", price), 1)
    
    # Verify
    assert order.total().amount == price.amount
    assert order.total().currency == price.currency
    

# Feature Suggestion: Free Shipping Threshold
# Description: Orders over a certain amount get free shipping.
# Orders with total >= 1000 USD qualify for free shipping



@pytest.fixture
def qualifying_order():
    customer = Customer("1", "John")
    order = Order("1", customer)
    price = Money(1000, "USD")
    order.add_product(Product("1", "Laptop", price), 1)
    return order

@pytest.fixture
def non_qualifying_order():
    customer = Customer("1", "John")
    order = Order("1", customer)
    price = Money(25, "USD")
    order.add_product(Product("1", "Book", price), 1)
    return order



def test_order_qualifies_for_free_shipping(qualifying_order):
    assert qualifying_order.free_shipping() == True

def test_order_below_threshold_no_free_shipping(non_qualifying_order):
    assert non_qualifying_order.free_shipping() == False


def test_shipping_cost_free_for_qualifying_order(qualifying_order):
    assert qualifying_order.get_shipping_cost() == 0

def test_shipping_cost_charged_for_non_qualifying_order(non_qualifying_order):
    assert non_qualifying_order.get_shipping_cost() > 0    
