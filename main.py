from mce.domain.customer import Customer


orders = []

def create_order(customer_name, product_name, price, quantity):
    total = price * quantity
    orders.append({
        "customer_name": customer_name,
        "product": product_name,
        "price": price,
        "quantity": quantity,
        "total": total
    })
    
    
    
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





