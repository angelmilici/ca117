class BankAccount(object):

    next_account_number = 16555232
    total_lodgements = 0
    interest_rate = 0.043

    def __init__(self, surname='', forename='', balance=0, account_number=0):
        self.forename = forename
        self.surname = surname
        self.balance = balance
        self.account_number = BankAccount.next_account_number
        BankAccount.next_account_number += 1
        BankAccount.total_lodgements += 1

    def __str__(self):
        return 'Name: {:s} {:s}\nAccount number: {:d}\nBalance: {:.2f}'.format(self.surname, self.forename, self.account_number, self.balance)

    def __iadd__(self, b1):
        self.balance += int(b1)
        return self

    def apply_interest(self):
        self.balance *= (1 + self.interest_rate)

    def lodge(self, h):
        self.balance += h
        BankAccount.total_lodgements += 1
