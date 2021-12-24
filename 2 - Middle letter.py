def mid(string):
    if len(string)%2 != 0:
        return string[int((len(string)-1)/2)]
    else:
        return ''
