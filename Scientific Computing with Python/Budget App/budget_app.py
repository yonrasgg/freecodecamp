class Category:
    
    def __init__(self, name):
        self.name = name 
        self.ledger = list()
    
    def deposit(self, amount, description = " "):
        if description == None:
            self.ledger.append({"amount": amount, "description": " "})
        else:
            self.ledger.append({"amount": amount, "description": description})
            
    def withdraw(self, amount, description = " "):
        if self.check_funds(amount):
            if description == None:
                self.ledger.append({"amount": - amount, "description": ' '})
            else:
                self.ledger.append({'amount': - amount, 'description': description})         
            return True
        else:
            return False
        
    def get_balance(self):
        cash_available = 0
        for item in self.ledger:
            cash_available += item['amount']
    
    def transfer(self, amount, category):
        if withdraw:
            withdraw = self.withdraw(amount, f"Transfer to {category.name}")
            return True
        else:
            category.deposit(amount, f"Transfer from {self.name}")
            return False
                
def create_spend_chart(categories):
    pass