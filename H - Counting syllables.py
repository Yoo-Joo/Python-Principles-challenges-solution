def count(string):
    count = 0
    for i in string:
        if i == '-':
            count += 1
    return count + 1
