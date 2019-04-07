from stack_092 import Stack

lefties = '({['
righties = ')}]'
dictr = {v: k for k, v in zip(lefties, righties)}

def matcher(l):
    s = Stack()
    for c in l:
        if c in lefties:
            s.push(c)
        try:
            if c in righties and s.top() == dictr[c]:
                s.pop()
        except IndexError:
            return False
    if s.is_empty():
        return True
    return False
