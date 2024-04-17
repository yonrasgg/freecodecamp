class Category:
    def __init__(self, name):
        self.name = name 
        self.ledger = []  # list of varables
    
    def deposit(self, amount, description = " "):
        if description == None:
            self.ledger.append({"amount": amount, "description": ' '})
        else:
            self.ledger.append({"amount": amount, "description": description})
            
    def withdraw(self, amount, description = " "):
        if self.check_funds(amount):
            if description == None:
                self.ledger.append({"amount": -amount, "description": ' '})
            else:
                self.ledger.append({'amount': -(amount), 'description': description})         
            return True
        else:
            return False
        
def create_spend_chart(categories):
    pass