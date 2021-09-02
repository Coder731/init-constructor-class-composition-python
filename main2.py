class TicketMixin:
    """Mixin to calculate ticket price based on age"""
    def __init__(self, name, age):
        self.name =name
        self.age=age
    def calculate_ticket_price(self, age):
        if age<12:
            price = 0
        elif age<18:
            price = 15
        elif age<60:
            price = 20
        elif age>=60:
            price=10
        return price

class Customer(TicketMixin):
    """
    Create instance of Customer
    """
    def __init__(self, name, age):
        TicketMixin.__init__(self, name, age)
        #instance attribute
        self.name = name
        self.age = age
        
    def describe(self):
        return(f"{self.name} age {self.age} ticket price is {self.calculate_ticket_price(self.age)}")

customer = Customer("Ryan Phillips", 22)
print(customer.describe())


