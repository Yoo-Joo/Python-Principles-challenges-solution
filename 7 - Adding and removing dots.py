def add_dots(string):
    for i in string:
        dots = ".".join(string)
    return dots

def remove_dots(string):
    return string.replace('.', '')
