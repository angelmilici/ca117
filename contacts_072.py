class Contact(object):

    def __init__(self, name, phone, email):
        self.n = name
        self.p = phone
        self.e = email

    def __str__(self):
        return ' '.join((self.n, self.p, self.e))

class ContactList(object):

    def __init__(self):
        self.d = {}

    def add_contact(self, contact):
        self.d[contact.n] = contact

    def del_contact(self, n):
        if n in self.d:
            del self.d[n]

    def get_contact(self, n):
        if n in self.d:
            return str(self.d[n])
        else:
            return None

    def __str__(self):
        sort = [str(self.d[x]) for x in sorted(self.d)]
        return '\n'.join(['Contact list', '------------'] + sort)
