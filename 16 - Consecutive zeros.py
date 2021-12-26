def consecutive_zeros(string):
    count = 0
    res = 0
    for i in string:
        if i == "0":
            count += 1
            res = max(res, count)
        else:
            count = 0
    return res
