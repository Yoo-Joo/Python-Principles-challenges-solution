def double_letters(string):
    i = 0
    while i < len(string)-1:
        if string[i] == string[i+1]:
            return True
        i += 1
    return False
