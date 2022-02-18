class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, money_plus):
        self.balance += money_plus
    
    def widthdraw(self, money_minus):
        if self.balance >= money_minus:
            self.balance -= money_minus
        else:
            print(f'Not enough money on {self.owner}\'s balance')

    def __str__(self):
        return f'Owner: {self.owner}\nBalance: {self.balance}'

user = Account('Aisultan', 1000)
print(user)
user.deposit(31423)
print(user)
user.widthdraw(30000)
print(user)
user.widthdraw(2423)
print(user)
user.widthdraw(5)
