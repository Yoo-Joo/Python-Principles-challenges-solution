def online_count(dict):
    count = 0
    for i in dict:
        if dict[i] == 'online':
            count += 1
    return count
