from mce.domain.customer import Customer
from mce.domain.order import Order
from mce.domain.product import Product, PhysicalProduct
from mce.domain.money import Money
from mce.domain.invoice import Invoice
from mce.domain.shipping import ShippingCalculator, StandardShipping
from mce.application.checkout_service import CheckoutService
from mce.infrastructure.json_repository import JSONRepository
from mce.infrastructure.in_memory_repository import InMemoryRepository
from mce.domain.repository import OrderRepository
from mce.infrastructure.email_notfier import EmailNotifier
from mce.domain.discount import PercentageDiscount, FixedDiscount, LoyaltyDiscount, CompositeDiscount
from mce.domain.payment import CreditCardProcessor

# orders = []

# def create_order(customer_name, product_name, price, quantity):
#     total = price * quantity
#     orders.append({
#         "customer_name": customer_name,
#         "product": product_name,
#         "price": price,
#         "quantity": quantity,
#         "total": total
#     })
    
    
    
"""
A customer places an order containing multiple products.
Each product has a price.
An order contains multiple order lines.
Each line has a quantity.

Customer
Order
OrderLine
Product

Money

"""
order_id = "1"

customer = Customer("1", "John")
order = Order(order_id, customer)
prod = PhysicalProduct("1", "x", Money(10, "USD"), StandardShipping())
prod1 = PhysicalProduct("1", "y", Money(20, "USD"), StandardShipping())

order.add_product(prod, 1)
order.add_product(prod1, 2)


discount = CompositeDiscount([
    PercentageDiscount(),
    FixedDiscount(),
    LoyaltyDiscount() 
])


persistance_repository = JSONRepository()
# persistance_repository = InMemoryRepository()

order_repository = OrderRepository(persistance_repository)

checkout_service = CheckoutService(order_repository, 
                                   CreditCardProcessor(), EmailNotifier(), discount)


checkout_service.checkout(order) 


# loaded_order = order_repository.get(order_id)


# print(loaded_order.total())







