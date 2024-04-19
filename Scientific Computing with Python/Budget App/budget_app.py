def create_spent_chart(categories):
    return None

class Category:
    
    def __init__(self, name):
        self.name = name 
        self.ledger = list()
    
    def deposit(self, amount, description = " "):
        self.ledger.append({"amount": amount, "description": description})
            
    def withdraw(self, amount, description = " "):
        if self.check_funds(amount):
            self.ledger.append({'amount': - amount, 'description': description})         
            return True
        return False
        
    def get_balance(self):
        cash_available = 0
        for item in self.ledger:
            cash_available += item['amount']
            
        return cash_available
    
    def transfer(self, amount, category):
        if self.check_funds(amount):
             self.withdraw(-amount, f'Transfer to {category.name}')
             category.deposit(amount, f'Transfer from {self.name}')
             return True
        return False
        
    def check_funds(self, amount):
        return amount <= self.get_balance()
    
    def get_withdrawals(self):
        total = 0
        for item in self.ledger:
            if item['amount'] < 0:
                total += item['amount']
        return total
    
    def __str__(self):
        title = f'{self.name:*^30}\n'
        items = ''
        total = 0
        for item in self.ledger:
            items += f'{item["description"][0:23]:23}' + f'{item["amount"]:>7.2f}' + '\n'
            total += item['amount'] 
            
        output = title + items + 'Total: ' + str(total)
        return output    
    
    def truncate(n):
        multiplier = 10
        return int(n * multiplier) / multiplier
    
    def get_totals(categories):
        total = 0
        breakdown = []
        for category in categories:
            total += category.get_withdrawals()
        rounded = list(map(lambda x: truncate(x / total), breakdown))
        return rounded
                
def create_spend_chart(categories):
    res = 'Percentage spent by category\n'
    i = 100
    totals = getTotals(categories)