"""Banking Application"""
import sys
class Customer:
    bank_name='Durgasoft Bank'
    def __init__(self, name, balance=0):
        self.name=name
        self.balance=balance

    def deposit(self,amount):
        self.balance=self.balance+amount
        print('total balance is rs',self.balance)

    def withdraw(self, amount):
        if amount>self.balance:
            print('insufficient balance')
            sys.exit()

        self.balance=self.balance-amount

        print(' the amount after withdrawing is', self.balance)
print('welcome to', Customer.bank_name)

name=input('enter your name')
c=Customer(name)

while True:
    print('d=deposit\n w=withdraw\n e=exit')

    options=input('choose your options').lower()
    if options=='d':
        amount=int(input('enter amount to deposit'))
        c.deposit(amount)

    if options=='w':
        amount=int(input('enter the amount to withdraw'))
        if not (amount>0 and amount%100==0):
            print('amount should be within limit')
        else:
            break
        c.withdraw(amount)
    elif options=='e':
        print('thanks for banking')
        sys.exit()

    else:
        print('please input valid options')















