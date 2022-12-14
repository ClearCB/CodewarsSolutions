def comp(array1,array2):
    one_is_none = array1 == [] or array2 == []
    both_are_none = array1 == [] and array2 == []
    if both_are_none:
        return True
    if one_is_none:
        return False
    len_first = len(array1)
    len_second = len(array2)
    length = range (0,len_first)
    if len_first != len_second:
        return False
    index = 0
    
    for i in length:
        array1.sort(key = abs)
        array2.sort(key = abs)
        elem_first = array1[index]
        elem_second = array2[index]
        squared = elem_first ** 2
        if elem_second == squared:
            index +=1
            continue
        else:
            return False
    if index == len_first:
        return True
    else:
        return False
    




if __name__ == "__main__":
    print ("Testing")
    array1 = [121, 144, 19, 161, 19, 144, 19, 11]
    array2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
    assert comp(array1, array2) 
    array1 = [121, 144, 19, 161, 19, 144, 19, 11]
    array2 = [11*21, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
    assert comp(array1, array2) == False
    array1 = [121, 144, 19, 161, 19, 144, 19, 11]
    array2 = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]
    assert comp(array1, array2) == False
    array1 = [-161, -144, -144, -121, -11, 19, 19, 19]
    array2 = [121, 361, 361, 361, 14641, 20736, 20736, 25921]
    assert comp(array1, array2) == True
    print ("Passed")