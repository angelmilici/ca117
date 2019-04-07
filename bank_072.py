class BankAccount(object):

    def __init__(self, balance=0):
        self.balance = float(balance)

    def deposit(self, amnt):
        self.balance += amnt

    def withdraw(self, amnt):
        if amnt > self.balance:
            print('Insufficient funds available')
        else:
            self.balance -= amnt

    def __str__(self):
        return 'Your current balance is: {:.2f} euro'.format(self.balance)
