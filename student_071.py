class Student(object):

    def __init__(self, surname, forename, sid, modlist=[]):
        self.sid = sid
        self.surname = surname
        self.forename = forename
        self.modlist = modlist

    def add_module(self, arg):
        if arg not in self.modlist:
            self.modlist.append(arg)

    def del_module(self, arg):
        if arg in self.modlist:
            self.modlist.remove(arg)

    def print_details(self):
        print('ID: {:d}'.format(self.sid))
        print('Surname: {:s}'.format(self.surname))
        print('Forename: {:s}'.format(self.forename))
        print('Modules: {:}'.format(' '.join([str(c) for c in self.modlist])))
