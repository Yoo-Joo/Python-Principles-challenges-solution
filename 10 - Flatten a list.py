def flatten(l):
    result = []
    for i in l:
        for j in i:
            result.append(j)
    return result
