def get_row_col(string):
    board = {"1":0, "2":1, "3":2, "A":0, "B":1, "C":2}
    return (board[string[1]], board[string[0]])
