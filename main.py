from mce.domain.customer import Customer
from mce.domain.order import Order
from mce.domain.product import Product
from mce.domain.money import Money
from mce.domain.address import Address

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


customer = Customer("1", "John")
order = Order("1", customer)
prod = Product("1", "x", Money(10, "USD"))
prod1 = Product("1", "y", Money(20, "USD"))
order.add_product(prod, 1)
order.add_product(prod1, 2)

print(order)



order._lines.append(...)

order.add_product

order_lines = order.lines

