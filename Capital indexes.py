def capital_indexes(string):
    l = []
    for i, e in enumerate(string):
        if e.isupper():
            l.append(i)
    return l
