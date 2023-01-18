def count_char_in_string(x, c):
    list_d = []
    for str in x:
        count = str.count(c)
        list_d.append(count)
    return list_d

x = ['abba', 'babana', 'ann']
c = 'a'
d = count_char_in_string(x, c)
print(d) # [2, 3, 1]