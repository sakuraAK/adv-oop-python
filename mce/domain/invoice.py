from .order import Order

class Invoice:
    
    def __init__(self, order: Order):
        self._order = order
        
    
    def total(self):
        return self._order.total()
    
    def generate_text(self) -> str:
        """
        Generate a text representation of the invoice.
        
        Returns:
            str: A formatted string containing the invoice details.
        """
        pass
    