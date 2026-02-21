from .product import Product
from .money import Money

class OrderLine:
    
    def __init__(self, product: Product, quantity: int):
        self._product = product
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")
        self._quantity = quantity
    
    
    
    def line_total(self) -> Money:
        return self._product.price * self._quantity
    
    
    def __str__(self):
        return f"Product: {self._product}: {self._quantity}"
    
    def __repr__(self):
         return f"Product: {self._product}: {self._quantity}"