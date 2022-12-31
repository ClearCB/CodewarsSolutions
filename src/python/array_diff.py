def array_diff(whole_list, element_to_delete):
    for i in element_to_delete:
        while i in whole_list:
            whole_list.remove(i)   
    return whole_list




if __name__ == "__main__":
    print ("Testing")
    assert array_diff([1,2], [1]) == [2]
    assert array_diff([1,2,2], [1]) == [2,2]
    assert array_diff([1,2,2], [2]) == [1]
    assert array_diff([1,2,2], []) == [1,2,2]
    assert array_diff([], [1,2]) == []
    assert array_diff([1,2,3], [1, 2]) == [3]
    print ("Passed")