def count(string):
    dicc = {}
    for i in string:
        if i in dicc:
            continue
        else:
            i_count= string.count(i)
            dicc[i]=i_count
    return dicc

count ("javi vas de lao")