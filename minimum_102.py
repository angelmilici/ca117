def minimum(l):
    if len(l) == 1:
        return l[0]
    m = minimum(l[1:])
    if l[0] < m:
        return l[0]
    return m
