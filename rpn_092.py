from math import sqrt
from stack_092 import Stack

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

def neg(x):
    return -x

binops = {'+': add, '-': sub, '*': mul, '/': div}
uniops = {'n': neg, 'r': sqrt}

def calculator(l):
    s = Stack()
    for i in l.split():
        if i in binops.keys():
            y = s.pop()
            x = s.pop()
            s.push(binops[i](x, y))
        elif i in uniops.keys():
            s.push(uniops[i](s.pop()))
        else:
            s.push(float(i))
    return s.top()
