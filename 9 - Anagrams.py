def is_anagram(a, b):
    A = "".join(sorted(a))
    B = "".join(sorted(b))
    if A == B:
        return True
    else:
        return False
