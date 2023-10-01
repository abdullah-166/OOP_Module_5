class bank:
    def __init__(self,balance):
        self.balance = balance
        self.minwithdraw = 100
        self.maxwithdraw = 1000000

    def get_balance(self):
        return self.balance
    
    def deposit(self,amount):
        if amount>0:
            self.balance +=  amount

    def withdraw(self, amount):
        if amount < self.minwithdraw:
            print(f'you can not withdraw below {self.minwithdraw}')
        elif amount > self.maxwithdraw:
            print(f'you amount is more than {self.maxwithdraw}. You can not withdraw')
        else:
            self.balance -= amount
            print(f'here is your money {amount}')
            print(f'your balance after withdraw {self.get_balance()}')
        
brac = bank(15000)
# brac.withdraw(25)
# brac.withdraw(2000000)
brac.withdraw(5000)

ibbl = bank(5000)
ibbl.deposit(2000)
ibbl.deposit(500)
print(ibbl.get_balance())

        

