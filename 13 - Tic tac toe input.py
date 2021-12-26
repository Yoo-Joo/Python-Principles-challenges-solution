def get_row_col(string):
    dict = {"1":0, "2":1, "3":2, "A":0, "B":1, "C":2}
    return (dict[string[1]], dict[string[0]])
