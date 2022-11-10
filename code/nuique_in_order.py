def unique_in_order(iterable):
    if len(iterable) <=1:
        return list(iterable)
    listed_order= list(iterable)
    new_list = []
    actual_index = 0
    next_index = actual_index + 1
    for i in listed_order:
        actual_i = listed_order[actual_index]
        next_i =listed_order[next_index]
        if actual_i == next_i and next_index < len(iterable):
            actual_index = next_index
            next_index +=1
            if next_index == len (iterable):
                new_list.append(i)
                break
            else:
                continue
        else:
            actual_index = next_index
            next_index +=1
            new_list.append(i)
            if next_index == len (iterable):
                new_list.append(next_i)
                break
    return new_list
assert unique_in_order('AAAABBBCCDAABBB')== ['A','B','C','D','A','B']