def up_array(array):
    if array == []:
        return None
    if len (array) < 0:
        return None
    result = []
    number = 0
    elevator = len(array)-1
    for i in array:
        if i < 0:
            return None
        if len(str(i)) > 1:
            return None
        number += i*(10**elevator)
        elevator -= 1
    number = number + 1
    number = str(number)
    result = [int(i) for i in number]
    while array[0] == 0 and len(array) > 1:
        array.pop(0)
        result.insert(0,0)
    return result



if __name__ == "__main__":
    print("Testing")
    assert up_array([2,3,9]) == [2,4,0]
    assert up_array([9,9]) == [1,0,0]
    assert up_array([0,4,2]) == [0,4,3]
    assert up_array([0]) == [1]
    print("Passed")