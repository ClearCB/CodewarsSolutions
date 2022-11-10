def first_n_smallest(array,the_first):
    if the_first == 0:
        return []
    new_list = []
    array_copied = array.copy()
    array.sort()
    array_objective = array[0:the_first]
    array_objective_len = len(array[0:the_first])
    new_list_len = 0
    while new_list_len < array_objective_len:
        for i in array_copied:
            same_ammount = array_objective.count(i) == new_list.count(i)
            if new_list_len == array_objective_len:
                break
            if i in array_objective and not same_ammount:
                new_list.append(i)
                new_list_len += 1
    return new_list

if __name__ == "__main__":
    print ("Testing")
    assert first_n_smallest([1,2,3,4,5],3)==[1,2,3]
    assert first_n_smallest([5,4,3,2,1],3)==[3,2,1]
    assert first_n_smallest([1,2,3,1,2],3)==[1,2,1]
    assert first_n_smallest([1,2,3,-4,0],3)==[1,-4,0]
    assert first_n_smallest([1,2,3,4,5],0)==[]
    assert first_n_smallest([1,2,3,4,5],5)==[1,2,3,4,5]
    assert first_n_smallest([1,2,3,4,2],4)==[1,2,3,2]
    assert first_n_smallest([2,1,2,3,4,2],2)==[2,1]
    assert first_n_smallest([2,1,2,3,4,2],3)==[2,1,2]
    assert first_n_smallest([-3,-10, -8, -8, 4, -7, -10, -8, -6, -6,-9, -10, -10, -4, -5, -6],7)==[-10, -8, -8, -10, -9, -10, -10]
    print ("Passed")