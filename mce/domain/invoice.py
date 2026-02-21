from .order import Order

class Invoice:
    
    def __init__(self, order: Order):
        self._order = order
        
    
    def total(self):
        return self._order.total()
    
    def generate_text(self) -> str:
        result = ""
        for line in self._order.lines:
            result += line
            result += "\n"            
        return result
        # return "\n".join([line for line in self._order.lines])
    