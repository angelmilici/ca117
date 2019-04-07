class BankAccount(object):

    next_account_number = 16555232
    account_type = 'General'

    def __init__(self, forename, surname, balance):
        self.f = forename
        self.s = surname
        self.b = float(balance)
        self.a = BankAccount.next_account_number
        BankAccount.next_account_number += 1

    def lodge(self, h):
        self.b += h

    def withdraw(self, h):
        if h > self.b:
            print('Insufficient funds available')
        else:
            self.b -= h

    def __str__(self):
        return 'Name: {:s} {:s}\nAccount number: {:d}\nAccount type: {:s}\nBalance: {:.2f}'.format(self.f, self.s, self.a, self.account_type, self.b)

class CurrentAccount(BankAccount):

    account_type = 'Current'
    overdraft = -1000.00

    def withdraw(self, h):
        new_balance = self.b - h
        if new_balance < self.overdraft:
            print('Insufficient funds available')
        else:
            self.b -= h

    def __str__(self):
        return 'Name: {:s} {:s}\nAccount number: {:d}\nAccount type: {:s}\nBalance: {:.2f}\nOverdraft: {:.2f}'.format(self.f, self.s, self.a, self.account_type, self.b, self.overdraft)

class SavingsAccount(BankAccount):

    interest_rate = 0.01
    account_type = 'Savings'

    def apply_interest(self):
        self.b *= (1 + self.interest_rate)

    def __str__(self):
        return 'Name: {:s} {:s}\nAccount number: {:d}\nAccount type: {:s}\nBalance: {:.2f}\nInterest rate: {:.2f}'.format(self.f, self.s, self.a, self.account_type, self.b, self.interest_rate)
