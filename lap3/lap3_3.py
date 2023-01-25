def is_plusone_dictionary(dict):
    list = []
    for key, value in dict.items():
        list.append(key)
        list.append(value)
    
    for i in range(1,len(list)):
        if list[i] - list[i-1] != 1:
            return False
    return True

